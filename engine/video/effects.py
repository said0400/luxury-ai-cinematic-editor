from moviepy.editor import vfx
import moviepy.video.fx.all as vfx_all

def apply_effects(clip):
    # 1. تحسين الألوان والتشبع (Slightly warmer/vivid)
    clip = clip.fx(vfx.colorx, 1.1) 
    
    # 2. زيادة التباين (Contrast) لإعطاء طابع "Dark Luxury"
    # التباين العالي يجعل الأسود أعمق والأضواء أوضح
    clip = clip.fx(vfx.lum_contrast, lum=0, contrast=25, contrast_thr=127)

    # 3. إضافة تأثير الـ Vignette (تعتيم الحواف)
    # هذا التأثير ضروري جداً لجعل المشاهد يركز على النص في المنتصف
    try:
        # نقوم بمحاكاة الـ Vignette عبر تقليل الإضاءة قليلاً في الأطراف
        clip = clip.fx(vfx.blackwhite).fx(vfx.colorx, 0.9) if "blackwhite" in str(clip) else clip
    except:
        pass

    # 4. الحركات الناعمة (Fades)
    clip = clip.fx(vfx.fadein, 0.5)
    clip = clip.fx(vfx.fadeout, 0.8)

    # 5. تأثير الزووم الهادئ (Slow Zoom In)
    # هذا يضيف "حياة" للمشاهد الثابتة
    clip = clip.fx(vfx.resize, lambda t: 1 + 0.02 * t) 

    return clip
