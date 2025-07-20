import bpy
from ..placement.tile_placer import TilePlacer

class CLG_OT_generate_layout(bpy.types.Operator):
    bl_idname = "clg.generate_layout"
    bl_label = "Generate Layout"
    bl_description = "Generate layout based on current settings"

    def execute(self, context):
        # Placeholder for calling functions from src/core
        # Added for testing pourposes
        tp = TilePlacer(None, context.scene.clg_tiles)
        tile = context.scene.clg_tiles[0]
        new_tile_collection = tp.copy_bl_tile(tile)
        tp.move_bl_tile(new_tile_collection, 1.0, 5.0, 0.0)

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
        for obj in context.selected_objects:
            obj_ref = tile.objects.add()
            obj_ref.object_ref = obj
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

class CLG_OT_normalize_frequency(bpy.types.Operator):
    bl_idname = "clg.normalize_frequency"
    bl_label = "Normalize Frequency"
    bl_description = "Normalize frequencies so that the sum will be equal to 1 while retaining ratios"

    def execute(self, context):
        zones = context.scene.clg_zones
        if not zones:
            self.report({'WARNING'}, "No zones to normalize")
            return {'CANCELLED'}
        
        frequencies = [zone.frequency for zone in zones]
        total = sum(frequencies)
        
        if total > 0:
            for zone in zones:
                zone.frequency = zone.frequency / total
        else:
            equal_freq = 1.0 / len(zones) if len(zones) > 0 else 0.0
            for zone in zones:
                zone.frequency = equal_freq

        return {'FINISHED'}

class CLG_OT_toggle_tile_in_zone(bpy.types.Operator):
    bl_idname = "clg.toggle_tile_in_zone"
    bl_label = "Toggle Tile"
    bl_description = "Toggle tile in selected zone, if tile is not toggled it won't be generated in the selected zone"
    tile_index: bpy.props.IntProperty() # type: ignore

    def execute(self, context):
        scene = context.scene
        tile = scene.clg_tiles[self.tile_index]
        zone = scene.clg_zones[scene.clg_active_zone_index] if scene.clg_zones else None

        if not zone:
            self.report({'ERROR'}, "No active zone selected")
            return {'CANCELLED'}

        tile_in_zone = None
        for zone_tile in zone.tiles:
            if zone_tile.name == tile.name:
                tile_in_zone = zone_tile
                break

        if tile_in_zone:
            index = zone.tiles.find(tile_in_zone.name)
            zone.tiles.remove(index)
            self.report({'INFO'}, f"Removed {tile.name} from zone {zone.name}")
        else:
            new_tile = zone.tiles.add()
            new_tile.name = tile.name
            new_tile.tile_type = tile.tile_type
            self.report({'INFO'}, f"Added {tile.name} to zone {zone.name}")

        return {'FINISHED'}

class CLG_OT_add_obj_ref(bpy.types.Operator):
    bl_idname = "clg.add_obj_ref"
    bl_label = "Add Object Reference"

    def execute(self, context):
        tile = context.scene.clg_tiles[context.scene.clg_active_tile_index]
        obj_ref = tile.objects.add()
        if context.active_object:
            obj_ref.object_ref = context.active_object
        return {'FINISHED'}

class CLG_OT_delete_obj_ref(bpy.types.Operator):
    bl_idname = "clg.delete_obj_ref"
    bl_label = "Delete Object Reference"

    def execute(self, context):
        tile = context.scene.clg_tiles[context.scene.clg_active_tile_index]
        index = tile.active_obj_ref_index
        if len(tile.objects) > 0 and index < len(tile.objects):
            tile.objects.remove(index)
            tile.active_obj_ref_index = min(max(0, index - 1), len(tile.objects) - 1)
        return {'FINISHED'}

classes = (
    CLG_OT_generate_layout,
    CLG_OT_add_zone,
    CLG_OT_delete_zone,
    CLG_OT_add_tile,
    CLG_OT_delete_tile,
    CLG_OT_normalize_frequency,
    CLG_OT_toggle_tile_in_zone,
    CLG_OT_add_obj_ref,
    CLG_OT_delete_obj_ref,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
