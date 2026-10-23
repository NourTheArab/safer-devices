<div dir="rtl" lang="ar">

# مراجعة المصادر المطلوبة لكل فحص عملي

[English](../sources/INCIDENT-REVIEW.md) · [فحوص الحوادث](incident-checks.md)

تاريخ اللقطة: **23 تشرين الأول 2026**. هذه قائمة مراجعة، وليست قائمة تثبيت. التحقق من المحتوى الحالي وانطباقه يسبق الفحص أو اقتراح الإصلاح. قراءة الرابط لا تساوي اختبار الجهاز.

## سجل المراجعة المطلوب

لكل بند منطبق، سجل خاص للرابط وتاريخ الوصول ومعرف التنبيه أو الإصدار والمنتج والفرع والمنصة ودليل التثبيت والفحص والنتيجة والإصلاح والتحقق. تعذر المصدر يُذكر صراحة بلا اختراع محتواه. يمكن استخدام تنبيه أصلي مستقل متاح، بلا تجاوز لضوابط الوصول. عدم الانطباق يحتاج سببًا من الحصر الفعلي.

| المصدر | العمل المطلوب منه |
|---|---|
| [قائمة Dom](https://github.com/dominikmartn/black-october-check) و[النص الأصلي](https://gist.github.com/dominikmartn/629ef73b1ebca67a0d0d4938a932a371) | مراجعة الفحوص والإصلاحات والتاريخ والفجوات، وتأكيد الادعاءات بالمصادر الأصلية، وترجمة المناسب إلى خطة محددة؛ لا تنفيذ جماعي أعمى. |
| [Wardlatch](https://github.com/deimos-hq/wardlatch) | الحوادث الحالية والمصدر والإصدار والأنظمة والخصوصية والخيارات. اقتراح نسخة محددة وفحص حادث محدود عند الحاجة؛ بلا مسح شامل أو محرك بعيد افتراضيًا. |
| [emudhra-check](https://github.com/wakumo/emudhra-check) | بديل للمراجعة، لا تثبيت إضافي تلقائي. التوثيق المقروء يذكر 12 موقع حادث وسجلات على سطح المكتب وإنشاء حاويات Docker ما لم يُعطل. مطابقة المجموعة الحالية ذات 14 موقعًا لازمة. أنبوب التنزيل إلى الطرفية والإصلاح الواسع غير مفوضين؛ مراجعة ملف محلي مثبت المصدر ونطاق السجلات والشبكة تسبق اقتراح التنفيذ. |
| [fort](https://github.com/djadmin/fort) | مراجعة فجوات إعدادات ماك وسلوك القراءة والمعاينة والإصلاح. الأدوات المدمجة أولًا، والتثبيت والتغييرات والتقارير الخاصة بنطاق منفصل. |
| [LuLu](https://github.com/objective-see/LuLu) و[دليل الناشر](https://objective-see.org/products/lulu.html) | عند وجوده أو اقتراحه، مراجعة النسخة والقواعد دون تاريخ وجهات خاص. شرح أثر الحظر على الميزات؛ لا تعديل افتراضيًا. |
| [تنبيه Node](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) و[مشكلة Bun](https://github.com/oven-sh/bun/issues/46352) و[إصدارات Brotli](https://github.com/google/brotli/releases) | النسخ المنفصلة والمضمّنة والعاملة؛ المؤشرات النصية قرائن فقط، مع الناشر والمصدر والمكتبة الفعلية. |
| [موزيلا وeMudhra](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/) و[مواقع الحادث](https://emudhra.we-have-a-problem.com/) | حصر العملاء والمخازن ومجموعة الاختبار الحالية وموافقة الشبكة وضوابط الفحص. لا تعميم على مخزن غير مفحوص. |
| [Go](https://go.dev/doc/devel/release) و[Java](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) و[pip](https://pip.pypa.io/en/stable/news/) و[uv](https://github.com/astral-sh/uv/releases) | كل بيئة وأداة تثبيت ونسخة تطبيق قائمة وفرع مدعوم وحالة العملية بعد التحديث. تحديث نسخة لا يغطي البقية. |
| [Tailscale](https://tailscale.com/security-bulletins) و[Electron](https://github.com/electron/electron/security/advisories) | مطابقة التطبيق والخدمة والإصدار وإعادة التشغيل. لا تغيير للأدوات الذكية أو أطر موقعة بلا موافقة محددة. |
| [إعلانات PHP](https://www.php.net/archive/2026.php) و[التنبيه الأول](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) و[الثاني](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) و[ووردبريس](https://wordpress.org/news/2026/10/critical-php-security-release/) | السؤال عن تشغيل موقع ومكان البيئة العاملة لطلبات الويب، ومتابعة إرشادات الإعدادات. تحديث متصفح أو إضافة أو طرفية لا يثبت إصلاح خدمة PHP. |
| [Next.js](https://nextjs.org/blog/nextjs-security-update-october-14-2026) و[Storybook](https://github.com/storybookjs/storybook/security/advisories/GHSA-f2ph-cmg5-wxc8) و[GitLab](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) و[Ruby](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/) | المشاريع والخدمات المتفق عليها عند وجودها، وبيانات النسخ دون خطافات تثبيت. البنية البعيدة تحتاج تفويضًا وخطة صيانة. |
| [حادث OVHcloud CLI](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw) و[LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026) و[حادث npm الأقدم](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/) | الفصل بين منتج ضعيف وملف خبيث فعلي، وبيانات المصدر دون تشغيل. التعرض المؤكد يحتاج أدلة واسترداد وصول، لا ترقية فقط. مثال npm من أيلول 2025. |
| [إفصاح Railway](https://blog.railway.com/p/security-disclosure-wednesday-october-21st) و[تقرير PingCAP/TiDB](https://www.pingcap.com/trust-hub/security/security-update-october-2026/) | السؤال عن الاستخدام وتخزين بيانات اعتماد، ومطابقة إرشادات المزود والحالة الخاصة بلا قراءة الأسرار. خدمات أخرى مثل OpenCode Console وFireworks AI وTreg تحتاج إشعارًا أصليًا حاليًا قبل ادعاء التعرض؛ الادعاء الصحفي أو الخاص وحده غير متحقق هنا. |
| [Docker](https://docs.docker.com/engine/security/) و[Colima](https://github.com/abiosoft/colima) | سياق محلي وحالة توقف أو عمل أولًا، ثم بيانات مختارة للصورة والإعداد ضمن النطاق. بلا تشغيل افتراضي أو أوامر داخل الحاوية أو حذف. |
| [إصدارات آبل الأمنية](https://support.apple.com/en-us/100100) و[ويندوز](https://learn.microsoft.com/en-us/windows/release-health/) و[أندرويد](https://support.google.com/android/answer/7680439) | دعم الجهاز والتحديث المنطبق واكتمال إعادة التشغيل، مع تضمين iPadOS صراحة لآيباد. |
| [إرشادات NCSC للأدوات الذكية](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai) و[طلب المساعدة](getting-help.md) | الحدود التقنية والرقابة وتصعيد الحوادث. نص التعليمات وحده ليس فرضًا تقنيًا ولا فحصًا جنائيًا. |

القائمة ليست شاملة لكل الإنترنت. البرامج المكتشفة الجديدة تحتاج متابعة مراجع أصلية ضمن نطاق محدود. لا تفويض لمسح عشوائي أو مستودع آخر أو تشغيل كل الأدوات. البدائل لفحص eMudhra أو ماك تحتاج مراجعة المصدر والخصوصية والنطاق والموافقة نفسها.

## توفر المصادر وحدود المراجعة

تعذر جلب النص الأصلي وصفحة OpenJDK وتنبيهي Next.js وRuby عبر أداة البحث أثناء التحديث. توفر مستودع Dom ومصادر أصلية أخرى؛ لا نقل لادعاءات أرقام تصحيح من صفحة غير مقروءة. سجل حزمة Wardlatch في المستودع يذكر 0.1.8، لكن نقطة إصدار npm لم تتوفر؛ لا ادعاء بالتحقق من الحزمة المنشورة ولا تثبيت مقيد بها هنا. مطابقة النسخة ومصدرها تسبق التشغيل.

هذه مراجعة توثيق ومصادر، لا تدقيق مستقل كامل للشيفرة ولا تزكية لكل أداة. لكل فحص لاحق تاريخ مراجعة جديد؛ لقطة 2026 ليست إثبات أمان دائمًا.

## مشاريع أخرى ذُكرت سابقًا

تعذرت قراءة [ملف فحص ماك من fexxdev](https://github.com/fexxdev/macos_secuirty_audit/blob/master/README.md) عبر الموصل. لم تُتحقق الهوية الدقيقة لمشروعي One2N security_scripts وGunnarMUC/MacAudit في هذه المراجعة. ليست اعتماديات معتمدة أو توصيات تشغيل. يلزم الرابط الأصلي الدقيق والمصدر والإصدار والسلوك؛ تشابه الاسم ليس بديلًا. هذه الفجوات لا تمنع الفحوص المدمجة أو مسار الحوادث المراجع.

</div>
