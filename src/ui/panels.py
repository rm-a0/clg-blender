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
        scene = context.scene
        zones = scene.clg_zones

        layout.label(text="Zones and Frequencies") 
        row = layout.row(align=True)
        
        col1 = row.column()
        box = col1.box()
        
        box.template_list(
            "UI_UL_list",
            "clg_zones_list",
            scene,
            "clg_zones",
            scene,
            "clg_active_zone_index",
            rows=3
        )
        
        if zones and 0 <= scene.clg_active_zone_index < len(zones):
            active_zone = zones[scene.clg_active_zone_index]
            box.prop(active_zone, "frequency", text="Frequency", slider=True)
        
        total_freq = sum(zone.frequency for zone in zones)
        box.label(text=f"Total Frequency: {total_freq:.3f}")
        
        col2 = row.column(align=True)
        col2.ui_units_x = 1.0
        col2.alignment = 'CENTER'
        
        button_col = col2.column(align=True)
        button_col.ui_units_x = 1.0
        button_col.operator("clg.add_zone", text="", icon='ADD')
        button_col.operator("clg.delete_zone", text="", icon='X')

class CLG_PT_zone_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Zone Settings"
    bl_idname = "CLG_PT_zone_settings"
    bl_parent_id = "CLG_PT_secondary_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
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
    CLG_PT_generate_panel,
    CLG_PT_zone_settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)