import bpy
from .properties import normalize_frequencies

class CLG_OT_generate_city(bpy.types.Operator):
    bl_idname = "clg.generate_city"
    bl_label = "Generate City"
    bl_description = "Generate the city layout based on current settings"

    def execute(self, context):
        print("TODO")
        self.report({'INFO'}, "City generation triggered")
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


classes = (
    CLG_OT_generate_city,
    CLG_OT_add_zone,
    CLG_OT_delete_zone,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
