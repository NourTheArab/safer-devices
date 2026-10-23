<div dir="rtl" lang="ar">

# المصادر والأدوات الاختيارية

[الدليل الرئيسي](../README.ar.md) · [English](../sources/README.md)

تاريخ مراجعة المصادر: **23 تشرين الأول 2026**. المرجع الحالي للمنتج والنظام والإصدار يسبق أي ملخص قديم. إدراج مصدر لا يعني تدقيق برامجه بالكامل أو ملاءمة كل توصياته للجميع. بعض التوثيق المرتبط بالإنكليزية.

## البداية

| المصدر | فائدته |
|---|---|
| [خطة الأمان من EFF](https://ssd.eff.org/module/your-security-plan) | اختيار الحماية وفق الاحتياجات والمخاطر الفعلية. |
| [النسخ الاحتياطي من NCSC](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/always-back-up-your-most-important-data) | تخطيط نسخ منفصلة وتجربة الاستعادة. |
| [خط المساعدة من Access Now](https://www.accessnow.org/help/) | دعم متخصص للمجتمع المدني والعمل الصحفي وحقوق الإنسان، وفق شروط الأهلية الحالية. |

## التوثيق الرسمي

- الحسابات: [غوغل والتحقّق بخطوتين](https://support.google.com/accounts/answer/185839?hl=ar)، [جلسات غوغل](https://support.google.com/accounts/answer/3067630)، [صلاحيات التطبيقات](https://support.google.com/accounts/answer/13533235)، [آبل](https://support.apple.com/en-us/102660)، [مايكروسوفت](https://support.microsoft.com/en-us/accounts-billing/security/how-to-use-two-step-verification-with-your-microsoft-account)، [غيت هب](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)، [بروتون](https://proton.me/support/two-factor-authentication-2fa).
- المتصفح: [إضافات كروم](https://support.google.com/chrome/answer/2664769?hl=ar)، [صلاحيات فايرفوكس](https://support.mozilla.org/en-US/kb/permission-request-messages-firefox-extensions)، [وصول الإضافة للنوافذ الخاصة](https://support.mozilla.org/en-US/kb/extensions-private-browsing)، [إضافة OpenAI](https://learn.chatgpt.com/docs/chrome-extension).
- ماك: [التحديث](https://support.apple.com/en-us/108382)، [التشفير](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac)، [الجدار الناري](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac)، [النسخ الاحتياطي](https://support.apple.com/en-us/104984).
- ويندوز: [حالة الإصدارات](https://learn.microsoft.com/en-us/windows/release-health/)، [أمان ويندوز](https://support.microsoft.com/en-us/windows/help-protect-my-device-with-windows-security-1a5b8102-c93d-0573-8fd3-b2d33a1e5386)، [الجدار الناري](https://support.microsoft.com/en-us/windows/security/windows-security/firewall-and-network-protection-in-the-windows-security-app)، [التشفير](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows).
- الهواتف: [تحديث آيفون](https://support.apple.com/en-us/118575)، [تحديث أندرويد وتصحيحات الأمان](https://support.google.com/android/answer/7680439)، [إشعارات تهديد آبل](https://support.apple.com/en-us/102174)، [نمط المنع](https://support.apple.com/en-us/105120).

## مشاريع اختيارية

| المشروع | النطاق والحدود |
|---|---|
| [Wardlatch](https://github.com/deimos-hq/wardlatch) | فحوص لحوادث محددة، منها شهادات الاتصال وبيئات التشغيل. التوثيق الحالي يستهدف ماك ولينكس، ويصف دعم ويندوز بأنه غير مكتمل أو غير مدعوم. الفحوص تتصل بمواقع عامة. اكتشاف الحاويات قد يصل لمحرك بعيد حسب السياق النشط؛ خيار `--no-containers` يستحق المراجعة عند حصر النطاق محليًا. |
| [fort](https://github.com/djadmin/fort) | فحص إعدادات ماك. يصف الناشر الفحص بأنه محلي بلا اتصالات، ويوثّق وضع معاينة. خيارات الإصلاح تعدّل الإعدادات. التقارير قد تتضمن هوية الجهاز ورقمه التسلسلي، ومكانها خاص. النتيجة ليست شهادة امتثال أو خلو من الاختراق. |
| [LuLu](https://github.com/objective-see/LuLu) | جدار ناري إضافي لماك لضبط اتصالات التطبيقات. التثبيت وتعديل القواعد قرار مقصود؛ المنع قد يعطّل المزامنة أو التحديثات. [دليل الناشر](https://objective-see.org/products/lulu.html). |
| [قائمة Dom](https://github.com/dominikmartn/black-october-check) | فحوص تقنية وإصلاحات لحوادث تشرين الأول 2026. مصدر إلهام، وليس قائمة دائمة بإصدارات آمنة. قد تتطلب الإصلاحات صلاحيات إدارة أو إعادة تشغيل أو تعديل الثقة بالشهادات. [النص الأصلي](https://gist.github.com/dominikmartn/629ef73b1ebca67a0d0d4938a932a371). |
| [أمان Docker](https://docs.docker.com/engine/security/) و[Colima](https://github.com/abiosoft/colima) | توثيق المحرك والعزل والجهاز الافتراضي. تشغيل جهاز قائم قد يعيد أعباء العمل تلقائيًا. |

المراجعة شملت التوثيق المرتبط، وليست تدقيقًا كاملًا للشيفرة أو ضمانًا. المطلوب قراءة المصدر والإصدار المحددين قبل الموافقة على التثبيت أو التشغيل. أدوات تشغيل الحزم مثل `npx` قد تنزّل شيفرة وتنفّذها. لا يتضمن هذا الدليل برنامج تثبيت عن بُعد.

## حداثة المصادر

لشرح الحوادث وأثرها والمقالات المرتبطة: [حوادث حديثة، بشرح واضح](why-this-matters.md).

مصادر أصلية جرت مراجعتها في **23 تشرين الأول 2026**:

- [إعلانات PHP المؤرّخة](https://www.php.net/archive/2026.php) و[التنبيه الحرج](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w): التصحيحات والمتابعة.
- [استجابة ووردبريس](https://wordpress.org/news/2026/10/critical-php-security-release/) و[إعلان ويكيميديا](https://diff.wikimedia.org/2026/10/21/impact-of-php-vulnerabilities-on-wikimedia-tools-and-services/): المسؤولية والأثر التشغيلي.
- [استجابة موزيلا لـ eMudhra](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/): حادثة الثقة بالشهادات.
- [تقرير غيت هب](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/): مثال أقدم مؤرّخ في أيلول 2025.
- [تحليل NCSC لموجة التصحيحات](https://www.ncsc.gov.uk/blogs/prepare-for-vulnerability-patch-wave) و[إرشادات أدوات المساعدة المستقلة](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai): الاستعداد وحدود الصلاحيات.
- [رواية OpenAI عن PHP](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/): رواية جهة مشاركة، وليست إثباتًا مستقلًا لكل توقع عن المخاطر المقبلة.

روابط الصحافة موسومة منفصلة في الشرح. تعذر جلب تقرير CNN بالعربية المقترح أثناء المراجعة، لذلك ليس دليل الادعاءات التقنية. تاريخ الخبر والضرر المؤكد والتوقع أمور منفصلة.

الأولوية لتنبيه الشركة أو البحث الأصلي، مع مطابقة المنتج والنظام وفرع الإصدار. تحديث المصدر قد يغيّر نطاق الفحص والمواقع والصلاحيات والإصدارات المصححة.

عند تعديل الدليل، يلزم تسجيل الصفحات المقروءة وتحديث تاريخ المراجعة فقط للمادة المعاد فحصها. أداة صيانة المستندات تفحص بنية هذا المستودع وروابطه المحلية فقط، ولا تفحص جهازًا أو صحة كل ادعاء أمني.

لا يضم المستودع نصوصًا أو برامج من المشاريع المرتبطة. تبقى تراخيصها ومسؤولية إصداراتها لدى الجهات الأصلية.

</div>
