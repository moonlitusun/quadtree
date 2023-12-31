from typing import List, Dict, Union

Rect = Dict[str, Union[int, float]]


class QuadTree:
    def __init__(
        self,
        bounds: Rect,
        max_objects: int = None,
        max_levels: int = 10,
        level: int = 4,
    ):
        self.max_objects = max_objects
        self.max_levels = max_levels

        self.bounds = bounds
        self.level = level or 0

        self.objects = []
        self.quadrants = []

    def split(self) -> None:
        next_level = self.level + 1
        sub_width = self.bounds["width"] / 2
        sub_height = self.bounds["height"] / 2
        x = self.bounds["x"]
        y = self.bounds["y"]

        # top right
        self.quadrants.append(
            QuadTree(
                {
                    "x": x + sub_width,
                    "y": y,
                    "width": sub_width,
                    "height": sub_height,
                },
                self.max_objects,
                self.max_levels,
                next_level,
            )
        )

        # top left
        self.quadrants.append(
            QuadTree(
                {
                    "x": x,
                    "y": y + sub_width,
                    "width": sub_width,
                    "height": sub_height,
                },
                self.max_objects,
                self.max_levels,
                next_level,
            )
        )

        # bottom left
        self.quadrants.append(
            QuadTree(
                {
                    "x": x,
                    "y": y + sub_height,
                    "width": sub_width,
                    "height": sub_height,
                },
                self.max_objects,
                self.max_levels,
                next_level,
            )
        )

        # bottom right
        self.quadrants.append(
            QuadTree(
                {
                    "x": x + sub_width,
                    "y": y + sub_height,
                    "width": sub_width,
                    "height": sub_height,
                },
                self.max_objects,
                self.max_levels,
                next_level,
            )
        )

    def getIndex(self, p_rect: Rect) -> List[int]:
        indexes = []
        bounds = self.bounds

        vertical_midpoint = bounds["x"] + bounds["width"] / 2
        horizontal_midpoint = bounds["y"] + bounds["height"] / 2

        start_is_north = p_rect["y"] < horizontal_midpoint
        start_is_west = p_rect["x"] < vertical_midpoint
        end_is_east = p_rect["x"] + p_rect["width"] > vertical_midpoint
        end_is_south = p_rect["y"] + p_rect["height"] > horizontal_midpoint

        if start_is_north and end_is_east:
            indexes.append(0)

        if start_is_west and start_is_north:
            indexes.append(1)

        if start_is_west and end_is_south:
            indexes.append(2)

        if end_is_east and end_is_south:
            indexes.append(3)

        return indexes

    def insert(self, p_rect: Rect) -> None:
        if self.quadrants:
            indexes = self.getIndex(p_rect)

            for k in indexes:
                self.quadrants[k].insert(p_rect)

            return

        self.objects.append(p_rect)

        if len(self.objects) <= self.max_objects or self.level > self.max_levels:
            return

        if not self.quadrants:
            self.split()

        for v in self.objects:
            indexes = self.getIndex(v)

            for kv in indexes:
                self.quadrants[kv].insert(v)

        self.objects = []

    def retrieve(self, p_rect: Rect) -> List[Rect]:
        indexes = self.getIndex(p_rect)
        return_objects = list(self.objects)

        if self.quadrants:
            for v in indexes:
                objects = self.quadrants[v].retrieve(p_rect)
                return_objects.extend(objects)

        return return_objects

    def clear(self):
        self.objects = []

        for v in self.quadrants:
            v.clear()

        self.quadrants = []
