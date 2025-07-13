import bpy

class CLG_UL_checkbox_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        scene = context.scene
        zone = scene.clg_zones[scene.clg_active_zone_index] if scene.clg_zones else None
        
        row = layout.row(align=True)
        row.label(text=item.name)
        
        is_in_zone = False
        if zone:
            for zone_tile in zone.tiles:
                if zone_tile.name == item.name:
                    is_in_zone = True
                    break

        row.operator(
           "clg.toggle_tile_in_zone", 
            text="",
            icon="CHECKBOX_HLT" if is_in_zone else "CHECKBOX_DEHLT"
        ).tile_index = index

class CLG_UL_obj_ref_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item.object_ref:
            layout.label(text=item.object_ref.name, icon='OBJECT_DATA')
        else:
            layout.label(text="None (Invalid reference)", icon='ERROR')

class CLG_PT_base_panel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CLG'

class CLG_PT_main_panel(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Custom Layout Generation"
    bl_idname = "CLG_PT_main_panel"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        pass

class CLG_PT_tile_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Tile Settings"
    bl_idname = "CLG_PT_tile_settings"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Tiles") 
        row = layout.row(align=True)
        
        col1 = row.column()
        box = col1.box()
        
        box.template_list(
            "UI_UL_list",
            "clg_tiles_list",
            scene,
            "clg_tiles",
            scene,
            "clg_active_tile_index",
            rows=3
        )
        
        col2 = row.column(align=True)
        col2.ui_units_x = 1.0
        col2.alignment = 'CENTER'
        
        button_col = col2.column(align=True)
        button_col.ui_units_x = 1.0
        button_col.operator("clg.add_tile", text="", icon='ADD')
        button_col.operator("clg.delete_tile", text="", icon='X')

class CLG_PT_tile_detail_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Tile Details"
    bl_idname = "CLG_PT_tile_detail_settings"
    bl_parent_id = "CLG_PT_tile_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tiles = scene.clg_tiles

        if not tiles or scene.clg_active_tile_index >= len(tiles):
            return

        tile = tiles[scene.clg_active_tile_index]

        layout.label(text=tile.name, icon='SNAP_FACE')
        layout.prop(tile, "name", text="Name")
        layout.prop(tile, "tile_type", text="Tile Type")

class CLG_PT_tile_object_references(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Object References"
    bl_idname = "CLG_PT_tile_object_references"
    bl_parent_id = "CLG_PT_tile_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tiles = scene.clg_tiles

        if not tiles or scene.clg_active_tile_index >= len(tiles):
            return

        tile = tiles[scene.clg_active_tile_index]
        row = layout.row(align=True)

        col1 = row.column()
        box = col1.box()
        box.template_list(
            "CLG_UL_obj_ref_list",
            "clg_obj_ref_list",
            tile,
            "objects",
            tile,
            "active_obj_ref_index",
            rows=3
        )

        col2 = row.column(align=True)
        col2.ui_units_x = 1.0
        col2.alignment = 'CENTER'
        button_col = col2.column(align=True)
        button_col.ui_units_x = 1.0
        button_col.operator("clg.add_obj_ref", text="", icon='ADD')
        button_col.operator("clg.delete_obj_ref", text="", icon='X')

class CLG_PT_tile_connections(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Tile Connections"
    bl_idname = "CLG_PT_tile_connections"
    bl_parent_id = "CLG_PT_tile_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tiles = scene.clg_tiles

        if not tiles or scene.clg_active_tile_index >= len(tiles):
            return

        tile = tiles[scene.clg_active_tile_index]

        col = layout.column(align=True)

        col.prop(tile, "top_connection", text="Top (Y)")
        col.prop(tile, "bottom_connection", text="Bottom (-Y)")
        col.prop(tile, "left_connection", text="Left (-X)")
        col.prop(tile, "right_connection", text="Right (X)")

class CLG_PT_primary_settings(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Primary Settings"
    bl_idname = "CLG_PT_primary_settings"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.prop(context.scene, "clg_grid_width", text="Grid Width (Tiles)")
        layout.prop(context.scene, "clg_grid_height", text="Grid Height (Tiles)")
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
        
        box_row = box.row(align=True)
        box_col1 = box_row.column()

        total_freq = sum(zone.frequency for zone in zones)
        box_col1.label(text=f"Total Frequency: {total_freq:.3f}")

        box_row.column()
        box_col2 = box_row.column(align=True)
        box_col2.operator("clg.normalize_frequency", text="Normalize")

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
        layout = self.layout
        scene = context.scene
        zones = scene.clg_zones

        if not zones or scene.clg_active_zone_index >= len(zones):
            layout.label(text="No zone selected.")
            return

        zone = zones[scene.clg_active_zone_index]
        layout.label(text="Allowed Tiles") 
        row = layout.row(align=True)
        
        col1 = row.column()
        box = col1.box()
        
        box.template_list(
            "CLG_UL_checkbox_list",
            "clg_tiles_list",
            scene,
            "clg_tiles",
            scene,
            "clg_active_tile_index",
            rows=3
        )

        layout.prop(zone, "path_generation", text="Path Generation")
        layout.prop(zone, "structure_generation", text="Structure Generation")
        
class CLG_PT_generate_panel(CLG_PT_base_panel, bpy.types.Panel):
    bl_label = "Generate"
    bl_idname = "CLG_PT_generate_panel"
    bl_parent_id = "CLG_PT_main_panel"
    bl_options = {'HIDE_HEADER'}
    bl_order = 100

    def draw(self, context):
        layout = self.layout
        layout.operator("clg.generate_layout", text="Generate", icon='PLAY')

classes = (
    CLG_UL_checkbox_list,
    CLG_PT_main_panel,
    CLG_PT_tile_settings,
    CLG_PT_tile_detail_settings,
    CLG_PT_primary_settings,
    CLG_PT_secondary_settings,
    CLG_PT_generate_panel,
    CLG_PT_zone_settings,
    CLG_UL_obj_ref_list,
    CLG_PT_tile_object_references,
    CLG_PT_tile_connections,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)