import bpy

class CITYGEN_PT_Placeholder(bpy.types.Panel):
    bl_label = "City Generator (WIP)"
    bl_idname = "CITYGEN_PT_placeholder"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CityGen'

    def draw(self, context):
        self.layout.label(text="Placeholder Label")

def register():
    bpy.utils.register_class(CITYGEN_PT_Placeholder)

def unregister():
    bpy.utils.unregister_class(CITYGEN_PT_Placeholder)