import bpy
from .properties import normalize_frequencies

class CLG_OT_generate_layout(bpy.types.Operator):
    bl_idname = "clg.generate_layout"
    bl_label = "Generate Layout"
    bl_description = "Generate layout based on current settings"

    def execute(self, context):
        print("TODO")
        self.report({'INFO'}, "Layout generation triggered")
        return {'FINISHED'}

class CLG_OT_add_zone(bpy.types.Operator):
    bl_idname = "clg.add_zone"
    bl_label = "Add Zone"
    bl_description = "Create new zone"

    def execute(self, context):
        zones = context.scene.clg_zones
        zone = zones.add()
        zone.name = f"Zone_0{len(zones)}"
        return {'FINISHED'}

class CLG_OT_delete_zone(bpy.types.Operator):
    bl_idname = "clg.delete_zone"
    bl_label = "Delete Zone"
    bl_description = "Delete selected zone"

    def execute(self, context):
        zones = context.scene.clg_zones
        index = context.scene.clg_active_zone_index
        if 0 <= index < len(zones):
            zones.remove(index)
            if index >= len(zones):
                context.scene.clg_active_zone_index = len(zones) - 1
        return {'FINISHED'}

class CLG_OT_add_tile(bpy.types.Operator):
    bl_idname = "clg.add_tile"
    bl_label = "Add Tile"
    bl_description = "Create new tile"

    def execute(self, context):
        tiles = context.scene.clg_tiles
        tile = tiles.add()
        tile.name = f"Tile_0{len(tiles)}"
        return {'FINISHED'}

class CLG_OT_delete_tile(bpy.types.Operator):
    bl_idname = "clg.delete_tile"
    bl_label = "Delete Tile"
    bl_description = "Delete selected tile"

    def execute(self, context):
        tiles = context.scene.clg_tiles
        index = context.scene.clg_active_tile_index
        if 0 <= index < len(tiles):
            tiles.remove(index)
            if index >= len(tiles):
                context.scene.clg_active_zone_index = len(tiles) - 1
        return {'FINISHED'}


classes = (
    CLG_OT_generate_layout,
    CLG_OT_add_zone,
    CLG_OT_delete_zone,
    CLG_OT_add_tile,
    CLG_OT_delete_tile,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
