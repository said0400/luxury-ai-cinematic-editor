from moviepy.editor import vfx


def apply_effects(clip):
    clip = clip.fx(vfx.colorx, 1.15)
    clip = clip.fx(vfx.lum_contrast, 10, 20)
    clip = clip.fx(vfx.fadein, 0.3)
    clip = clip.fx(vfx.fadeout, 0.3)

    return clip
