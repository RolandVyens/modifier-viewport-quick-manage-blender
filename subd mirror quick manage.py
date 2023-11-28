bl_info = {
    "name": "subd and mirror quick manage tool",
    "author": "GPT 3.5, Roland Vyens",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy


def apply_all_mirror_modifiers():
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == "MESH":
            for modifier in reversed(obj.modifiers):
                if modifier.type == "MIRROR":
                    bpy.context.view_layer.objects.active = obj
                    bpy.ops.object.modifier_apply(modifier=modifier.name)


def disable_subdivision_modifiers_in_viewport():
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == "MESH":
            for modifier in obj.modifiers:
                if modifier.type == "SUBSURF":
                    modifier.show_viewport = False


def enable_subdivision_modifiers_in_viewport():
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == "MESH":
            for modifier in obj.modifiers:
                if modifier.type == "SUBSURF":
                    modifier.show_viewport = True


class OBJECT_OT_apply_mirror_modifiers(bpy.types.Operator):
    bl_idname = "object.apply_mirror_modifiers"
    bl_label = "Apply Mirror"
    bl_description = "Apply all Mirror modifiers on selected objects"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        apply_all_mirror_modifiers()
        return {"FINISHED"}


class OBJECT_OT_disable_subdivision_modifiers_in_viewport(bpy.types.Operator):
    bl_idname = "object.disable_subdivision_modifiers_in_viewport"
    bl_label = "Disable Subdivision in Viewport"
    bl_description = (
        "Disable all selected objects' subdivision modifiers in the viewport"
    )
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        disable_subdivision_modifiers_in_viewport()
        return {"FINISHED"}


class OBJECT_OT_enable_subdivision_modifiers_in_viewport(bpy.types.Operator):
    bl_idname = "object.enable_subdivision_modifiers_in_viewport"
    bl_label = "Enable Subdivision in Viewport"
    bl_description = (
        "Enable all selected objects' subdivision modifiers in the viewport"
    )
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        enable_subdivision_modifiers_in_viewport()
        return {"FINISHED"}


def draw_func(self, context):
    layout = self.layout

    layout.operator(OBJECT_OT_apply_mirror_modifiers.bl_idname, icon="MOD_MIRROR")

    layout.operator(
        OBJECT_OT_disable_subdivision_modifiers_in_viewport.bl_idname,
        icon="MOD_SUBSURF",
    )

    layout.operator(
        OBJECT_OT_enable_subdivision_modifiers_in_viewport.bl_idname, icon="MOD_SUBSURF"
    )


classes = [
    OBJECT_OT_apply_mirror_modifiers,
    OBJECT_OT_disable_subdivision_modifiers_in_viewport,
    OBJECT_OT_enable_subdivision_modifiers_in_viewport,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.DATA_PT_modifiers.append(draw_func)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.DATA_PT_modifiers.remove(draw_func)


if __name__ == "__main__":
    register()
