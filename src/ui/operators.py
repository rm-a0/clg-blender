import bpy

class CLG_OT_generate_city(bpy.types.Operator):
    bl_idname = "clg.generate_city"
    bl_label = "Generate City"
    bl_description = "Generate the city layout based on current settings"

    def execute(self, context):
        print("TODO")
        self.report({'INFO'}, "City generation triggered!")
        return {'FINISHED'}

classes = (
    CLG_OT_generate_city,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
