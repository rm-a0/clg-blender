import bpy

class CLG_PT_base_panel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CityGen'

class CLG_PT_main_panel(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "City Layout Generation"
    bl_idname = "CLG_PT_main_panel"

    def draw(self, context):
        pass

class CLG_PT_tile_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Tile Settings"
    bl_idname = "CLG_PT_tile_settings"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        pass

class CLG_PT_primary_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Primary Settings"
    bl_idname = "CLG_PT_primary_settings"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.prop(context.scene, "clg_grid_width", text="City Width (Tiles)")
        layout.prop(context.scene, "clg_grid_height", text="City Height (Tiles)")
        layout.separator()
        layout.prop(context.scene, "clg_terrain_intensity", text="Terrain Intensity")
        layout.separator()
        layout.prop(context.scene, "clg_lake_frequency", text="Lake Frequency")
        layout.prop(context.scene, "clg_river_frequency", text="River Frequency")

class CLG_PT_secondary_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Secondary Settings"
    bl_idname = "CLG_PT_secondary_settings"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        pass

class CLG_PT_generate_panel(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Generate"
    bl_idname = "CLG_PT_generate_panel"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'HIDE_HEADER'}
    bl_order = 100

    def draw(self, context):
        layout = self.layout
        layout.operator("clg.generate_city", text="Generate", icon='PLAY')

classes = (
    CLG_PT_main_panel,
    CLG_PT_tile_settings,
    CLG_PT_primary_settings,
    CLG_PT_secondary_settings,
    CLG_PT_generate_panel
)

def register():
    bpy.types.Scene.clg_grid_width = bpy.props.IntProperty(
        name="Grid Width",
        default=10,
        min=1,
        description="Number of tiles in the grid width (width of the city in tiles)"
    )
    bpy.types.Scene.clg_grid_height = bpy.props.IntProperty(
        name="Grid Height",
        default=10,
        min=1,
        description="Number of tiles in the grid height (height of the city in tiles)"
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
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.clg_grid_width
    del bpy.types.Scene.clg_grid_height
    del bpy.types.Scene.clg_terrain_intensity
    del bpy.types.Scene.clg_lake_frequency
    del bpy.types.Scene.clg_river_frequency