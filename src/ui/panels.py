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
        pass

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
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)