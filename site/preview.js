"use strict";

// A copy convenience only. No analytics, storage, account access or device audit.
const copyButton = document.querySelector("[data-copy]");
if (copyButton) {
  copyButton.addEventListener("click", async () => {
    const prompt = document.querySelector("#audit-prompt");
    const status = document.querySelector("#copy-status");
    if (!prompt || !status) return;
    const arabic = document.documentElement.lang === "ar";
    try {
      await navigator.clipboard.writeText(prompt.textContent);
      copyButton.textContent = arabic ? "تم النسخ" : "Copied";
      status.textContent = arabic ? "النص جاهز للصق في أداة المساعدة، مع رابط المستودع عند نشره." : "Ready to paste into your agent. Include the repository URL when it is published.";
    } catch {
      const selection = window.getSelection();
      if (selection) {
        const range = document.createRange();
        range.selectNodeContents(prompt);
        selection.removeAllRanges();
        selection.addRange(range);
      }
      status.textContent = arabic ? "تعذر النسخ التلقائي. النص محدد للنسخ يدويًا." : "Automatic copying was unavailable. The prompt is selected for manual copying.";
    }
  });
}
