import bpy

def update_connection(self, context):
    pass

class CLG_PG_obj_ref(bpy.types.PropertyGroup):
    object_ref: bpy.props.PointerProperty(
        name="Object Reference",
        type=bpy.types.Object
    ) # type: ignore

class CLG_PG_tile(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Tile Name",
        default="Tile"
    )  # type: ignore
    tile_type: bpy.props.EnumProperty(
        name="Type",
        description="Type/category of a tile",
        items=[
            ('PATH', "Path", "Paths and roads"),
            ('WATER', "Water", "Rivers, lakes and bodies of water"),
            ('STRUCTURE', "Structure", "Building or any type of structure"),
            ('DECORATION', "Decoration", "Trees, lamps or any types of decorations"),
            ('CUSTOM', "Custom", "Custom or user-defined type"),
        ],
        default='STRUCTURE'
    )  # type: ignore
    objects: bpy.props.CollectionProperty(
        name="Tile Objects",
        type=CLG_PG_obj_ref
    )  # type: ignore
    active_obj_ref_index: bpy.props.IntProperty(
        name="Active Object Reference Index",
        default=0
    )  # type: ignore
    top_connection: bpy.props.EnumProperty(
        name="Top",
        description="Tile connected to the top side",
        items=[("NONE", "None", "No connection")],  # Static default item
        default="NONE",
        update=update_connection
    )  # type: ignore
    bottom_connection: bpy.props.EnumProperty(
        name="Bottom",
        description="Tile connected to the bottom side",
        items=[("NONE", "None", "No connection")],  # Static default item
        default="NONE",
        update=update_connection
    )  # type: ignore
    left_connection: bpy.props.EnumProperty(
        name="Left",
        description="Tile connected to the left side",
        items=[("NONE", "None", "No connection")],  # Static default item
        default="NONE",
        update=update_connection
    )  # type: ignore
    right_connection: bpy.props.EnumProperty(
        name="Right",
        description="Tile connected to the right side",
        items=[("NONE", "None", "No connection")],  # Static default item
        default="NONE",
        update=update_connection
    )  # type: ignore

class CLG_PG_zone(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Zone Name", 
        default="Zone"
    ) # type: ignore
    frequency: bpy.props.FloatProperty(
        name="Frequency",
        description="Frequency of selected zone in generated layout",
        default=0.0,
        min=0.0,
        max=1.0,
    ) # type: ignore
    tiles: bpy.props.CollectionProperty(
        name="Allowed Tiles",
        type=CLG_PG_tile,
    ) # type: ignore
    path_generation: bpy.props.EnumProperty(
        name="Secondary Path Generation",
        description="Algorithm for generating secondary paths",
        items=[
            ('NONE', "None", "No secondary paths will be generated"),
            ('VORONOI', "Voronoi", "Uses edges of voronoi diagrams for path generation"),
            ('GRID', "Grid", "Uses points with offset for generating grid-like path structure"),
            ('RADIAL', "Radial", "Creates circular paths with offset for generating radial path structure"),
            ('AI', "AI", "Uses AI trained on pictures of city layouts"),
        ],
        default='NONE'
    ) # type: ignore
    structure_generation: bpy.props.EnumProperty(
        name="Structure Generation",
        description="Algorithm for generating structures",
        items=[
            ('NONE', "None", "No strucutres will be generated"),
            ('GRID', "Grid", "Uses points with offset for generating structures in grid-like pattern"),
            ('RADIAL', "Radial", "Generates structures in raidal-like pattern"),
            ('AI', "AI", "Uses AI trained on pictures of city layouts"),
        ],
        default='NONE'
    ) # type: ignore

classes = (
    CLG_PG_obj_ref,
    CLG_PG_tile,
    CLG_PG_zone,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.clg_zones = bpy.props.CollectionProperty(type=CLG_PG_zone)
    bpy.types.Scene.clg_tiles = bpy.props.CollectionProperty(type=CLG_PG_tile)
    bpy.types.Scene.clg_active_tile_index = bpy.props.IntProperty(
        name="Active Tile Index",
        default=0,
        min=0,
        description="Index of the active tile in the UI list"
    )
    bpy.types.Scene.clg_active_zone_index = bpy.props.IntProperty(
        name="Active Zone Index",
        default=0,
        min=0,
        description="Index of the active zone in the UI list"
    )
    bpy.types.Scene.clg_grid_width = bpy.props.IntProperty(
        name="Grid Width",
        default=10,
        min=1,
        description="Number of tiles in the grid width (width of the layout in tiles)"
    )
    bpy.types.Scene.clg_grid_height = bpy.props.IntProperty(
        name="Grid Height",
        default=10,
        min=1,
        description="Number of tiles in the grid height (height of the layout in tiles)"
    )
    bpy.types.Scene.clg_terrain_intensity = bpy.props.IntProperty(
        name="Terrain Intensity",
        default=0,
        min=0,
        description="Intensity or strength of generated terrain \n(0 = no elevation, flat surface)"
    )
    bpy.types.Scene.clg_lake_frequency = bpy.props.IntProperty(
        name="Lake Frequency",
        default=0,
        min=0,
        description="Frequency of generated lakes \n(0 = no lakes generated)"
    )
    bpy.types.Scene.clg_river_frequency = bpy.props.IntProperty(
        name="River Frequency",
        default=0,
        min=0,
        description="Frequency of generated rivers \n(0 = no rivers generated)"
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.clg_tiles
    del bpy.types.Scene.clg_active_tile_index
    del bpy.types.Scene.clg_zones
    del bpy.types.Scene.clg_active_zone_index
    del bpy.types.Scene.clg_grid_width
    del bpy.types.Scene.clg_grid_height
    del bpy.types.Scene.clg_terrain_intensity
    del bpy.types.Scene.clg_lake_frequency
    del bpy.types.Scene.clg_river_frequency