import bpy

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

class CLG_PG_tile(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Tile Name",
        default="Tile"
    ) # type: ignore

def normalize_frequencies(context):
    zones = context.scene.clg_zones
    if not zones:
        return
    
    frequencies = [zone.frequency for zone in zones]
    total = sum(frequencies)
    
    if total == 0:
        equal_freq = 1.0 / len(zones) if len(zones) > 0 else 0.0
        for zone in zones:
            zone.frequency = equal_freq
    elif total >= 1.0:
        for zone in zones:
            zone.frequency = zone.frequency / total if total > 0 else 0.0

classes = (
    CLG_PG_zone,
    CLG_PG_tile,
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
    del bpy.types.Scene.clg_zones
    del bpy.types.Scene.clg_active_zone_index
    del bpy.types.Scene.clg_grid_width
    del bpy.types.Scene.clg_grid_height
    del bpy.types.Scene.clg_terrain_intensity
    del bpy.types.Scene.clg_lake_frequency
    del bpy.types.Scene.clg_river_frequency