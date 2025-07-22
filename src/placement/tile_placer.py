import bpy
from mathutils import Vector
from ..core.models.grid import Grid
from ..ui.properties import CLG_PG_tile

class TilePlacer:
    def __init__(self, grid: Grid, tile_collection: bpy.props.CollectionProperty):
        self.grid = grid
        self.tile_map = {tile.name: tile for tile in tile_collection}

    def copy_bl_tile(self, tile: CLG_PG_tile) -> bpy.types.Collection:
        new_collection = bpy.data.collections.new(f"{tile.name}_copy")
        bpy.context.scene.collection.children.link(new_collection)

        for obj_ref in tile.objects:
            if obj_ref.object_ref:
                new_obj = obj_ref.object_ref.copy()
                new_collection.objects.link(new_obj)

        return new_collection
    
    def hide_bl_tile(self, tile: CLG_PG_tile) -> None:
        for obj_ref in tile.objects:
            if obj_ref.object_ref:
                obj_ref.object_ref.hide_viewport = True
                obj_ref.object_ref.hide_render = True

    def hide_all_bl_tiles(self) -> None:
        for tile in self.tile_map.values():
            self.hide_bl_tile(tile=tile)

    # TODO: Remove debugging print after expanding and finalizing the method
    def move_bl_tile(self, collection: bpy.types.Collection, x: float, y: float, z: float) -> None:
        if not collection.objects:
            print("No objects in collection")
            return

        min_coords = Vector((float('inf'), float('inf'), float('inf')))
        max_coords = Vector((float('-inf'), float('-inf'), float('-inf')))
        has_valid_objects = False

        for obj in collection.objects:
            if obj.data and obj.data.vertices:
                bound_box = obj.bound_box
                matrix_world = obj.matrix_world
                for corner in bound_box:
                    world_corner = matrix_world @ Vector(corner)
                    min_coords.x = min(min_coords.x, world_corner.x)
                    min_coords.y = min(min_coords.y, world_corner.y)
                    min_coords.z = min(min_coords.z, world_corner.z)
                    max_coords.x = max(max_coords.x, world_corner.x)
                    max_coords.y = max(max_coords.y, world_corner.y)
                    max_coords.z = max(max_coords.z, world_corner.z)
                has_valid_objects = True

        if not has_valid_objects:
            print("No valid mesh objects found in collection")
            return

        bbox_center = (min_coords + max_coords) * 0.5
        print(f"Bounding box center: {bbox_center}")

        target_location = Vector((x, y, z))
        offset = target_location - bbox_center
        print(f"Calculated offset: {offset}")

        for obj in collection.objects:
            obj.location += offset
            print(f"Moved object {obj.name} to new location: {obj.location}")

    def place_tiles(self) -> None:
        bpy.ops.object.select_all(action='DESELECT')
        self.hide_all_bl_tiles()

        for row in range(self.grid.width):
            for col in range(self.grid.height):
                # Core refers to tiles from the 'core' module and bl refers to the actual tiles inside blender
                core_tile = self.grid.get_tile(row, col)
                core_tile_name = core_tile.definition.name

                if not core_tile_name or core_tile_name not in self.tile_map:
                    continue

                bl_tile = self.tile_map[core_tile_name]
                bl_collection = self.copy_bl_tile(bl_tile)
                self.move_bl_tile(bl_collection, float(row * core_tile.definition.width), float(col * core_tile.definition.height), float(core_tile.elevation))
