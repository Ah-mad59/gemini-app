<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مساعد معالجة النصوص الذكي</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
        body { font-family: 'Cairo', sans-serif; }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 min-h-screen text-gray-100 flex flex-col items-center justify-center p-4">

    <div class="w-full max-w-3xl bg-slate-800/80 backdrop-blur-xl border border-slate-700 shadow-2xl rounded-2xl p-6 md:p-8 space-y-6">
        
        <!-- Header -->
        <div class="text-center space-y-2">
            <div class="inline-flex items-center justify-center w-14 h-14 rounded-full bg-indigo-600/30 border border-indigo-500/30 text-indigo-400 text-2xl mb-2 shadow-inner">
                <i class="fa-solid fa-wand-magic-sparkles"></i>
            </div>
            <h1 class="text-2xl md:text-3xl font-extrabold tracking-tight text-white">مساعد معالجة النصوص الذكي</h1>
            <p class="text-sm text-gray-400">صحح، لخص، أو أعد صياغة نصوصك العربية بذكاء واحترافية</p>
        </div>

        <!-- Form -->
        <form action="/process" method="POST" class="space-y-4" onsubmit="showLoading()">
            <div>
                <label for="text" class="block text-sm font-medium text-gray-300 mb-1">أدخل النص هنا:</label>
                <textarea id="text" name="text" rows="5" required
                    class="w-full bg-slate-900/90 border border-slate-700 rounded-xl p-4 text-gray-100 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all shadow-inner resize-y"
                    placeholder="اكتب أو الصق النص العربي هنا لتتم معالجته...">{{ original_text if original_text else '' }}</textarea>
            </div>

            <div>
                <label for="action" class="block text-sm font-medium text-gray-300 mb-1">اختر العملية:</label>
                <div class="relative">
                    <select id="action" name="action"
                        class="w-full bg-slate-900/90 border border-slate-700 rounded-xl p-3.5 pr-4 pl-10 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all appearance-none cursor-pointer">
                        <option value="fix">✨ تصحيح الأخطاء والإملاء</option>
                        <option value="summarize">📊 تلخيص النص بذكاء</option>
                        <option value="rewrite">💡 إعادة صياغة بأسلوب احترافي</option>
                    </select>
                    <div class="absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none text-gray-400">
                        <i class="fa-solid fa-chevron-down text-xs"></i>
                    </div>
                </div>
            </div>

            <button type="submit" id="submit-btn"
                class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3.5 px-6 rounded-xl shadow-lg hover:shadow-indigo-500/25 transition-all duration-200 flex items-center justify-center gap-2 group cursor-pointer">
                <i class="fa-solid fa-bolt text-amber-300 group-hover:scale-110 transition-transform"></i>
                <span>تنفيذ العملية</span>
            </button>
        </form>

        <!-- Result Box -->
        {% if result %}
        <div class="mt-6 pt-6 border-t border-slate-700/80 space-y-3">
            <div class="flex items-center justify-between">
                <h2 class="text-lg font-bold text-indigo-400 flex items-center gap-2">
                    <i class="fa-solid fa-square-poll-vertical"></i>
                    النتيجة:
                </h2>
                <button type="button" onclick="copyResult()" class="text-xs bg-slate-700 hover:bg-slate-600 text-gray-300 px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 cursor-pointer">
                    <i class="fa-regular fa-copy"></i> نسخ النص
                </button>
            </div>
            <div id="result-text" class="w-full bg-slate-900/90 border border-slate-700 rounded-xl p-4 text-gray-200 whitespace-pre-wrap leading-relaxed shadow-inner">
                {{ result }}
            </div>
        </div>
        {% endif %}

    </div>

    <!-- Footer -->
    <footer class="mt-8 text-center text-xs text-gray-500">
        تم التطوير بواسطة الذكاء الاصطناعي • مدعوم بواسطة Gemini API
    </footer>

    <script>
        function showLoading() {
            const btn = document.getElementById('submit-btn');
            btn.disabled = true;
            btn.innerHTML = `<i class="fa-solid fa-spinner animate-spin"></i> <span>جاري المعالجة...</span>`;
        }

        function copyResult() {
            const text = document.getElementById('result-text').innerText;
            navigator.clipboard.text = text;
            navigator.clipboard.writeText(text).then(() => {
                alert('تم نسخ النص بنجاح!');
            });
        }
    </script>
</body>
</html>

