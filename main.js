// ===== Язык =====
(function () {
  const root = document.documentElement;
  const titles = {
    ru: document.body.dataset.titleRu,
    uz: document.body.dataset.titleUz,
  };

  function setLang(lang) {
    root.lang = lang;
    try { localStorage.setItem("lang", lang); } catch (e) {}
    if (titles[lang]) document.title = titles[lang];
    document.dispatchEvent(new CustomEvent("langchange", { detail: lang }));
  }

  document.querySelectorAll(".lang-switch button").forEach((btn) =>
    btn.addEventListener("click", () => setLang(btn.dataset.set))
  );
  setLang(root.lang || "ru");

  // ===== Мобильное меню =====
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav");
  if (burger) burger.addEventListener("click", () => nav.classList.toggle("open"));

  // ===== Появление блоков при прокрутке =====
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("show"); io.unobserve(e.target); }
    }),
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  // ===== Чек-лист эко-привычек =====
  const checks = document.querySelectorAll(".check input");
  if (checks.length) {
    let saved = {};
    try { saved = JSON.parse(localStorage.getItem("habits") || "{}"); } catch (e) {}
    const bar = document.querySelector(".progress-bar");
    const num = document.querySelectorAll(".progress-num");
    const update = () => {
      const done = [...checks].filter((c) => c.checked).length;
      bar.style.width = (done / checks.length) * 100 + "%";
      num.forEach((n) => (n.textContent = done + " / " + checks.length));
    };
    checks.forEach((c) => {
      c.checked = !!saved[c.id];
      c.addEventListener("change", () => {
        saved[c.id] = c.checked;
        try { localStorage.setItem("habits", JSON.stringify(saved)); } catch (e) {}
        update();
      });
    });
    update();
  }

  // ===== Квиз =====
  const quizEl = document.getElementById("quiz");
  if (quizEl && window.QUIZ) {
    const Q = window.QUIZ;
    let i = 0, score = 0;
    const L = (o) => `<span data-l="ru">${o.ru}</span><span data-l="uz">${o.uz}</span>`;

    function render() {
      if (i >= Q.length) {
        quizEl.innerHTML = `
          <div class="result">
            <span class="q-count">${L({ ru: "Результат", uz: "Natija" })}</span>
            <b>${score} / ${Q.length}</b>
            <p>${score >= 4
              ? L({ ru: "Отлично! Вы хорошо знаете, как беречь природу.", uz: "Ajoyib! Siz tabiatni asrashni yaxshi bilasiz." })
              : L({ ru: "Неплохо! Загляните на другие страницы сайта — там все ответы.", uz: "Yomon emas! Saytning boshqa sahifalarida barcha javoblar bor." })}</p>
            <button class="btn btn-primary next" id="restart">${L({ ru: "Пройти ещё раз", uz: "Qayta oʻtish" })}</button>
          </div>`;
        document.getElementById("restart").onclick = () => { i = 0; score = 0; render(); };
        return;
      }
      const q = Q[i];
      quizEl.innerHTML = `
        <span class="q-count">${L({ ru: "Вопрос", uz: "Savol" })} ${i + 1} / ${Q.length}</span>
        <h3>${L(q.q)}</h3>
        <div class="options">${q.a.map((a, k) => `<button data-k="${k}">${L(a)}</button>`).join("")}</div>`;
      quizEl.querySelectorAll(".options button").forEach((b) =>
        b.addEventListener("click", () => {
          const k = +b.dataset.k;
          quizEl.querySelectorAll(".options button").forEach((x) => {
            x.disabled = true;
            if (+x.dataset.k === q.c) x.classList.add("right");
          });
          if (k === q.c) score++; else b.classList.add("wrong");
          const next = document.createElement("button");
          next.className = "btn btn-primary next";
          next.innerHTML = L({ ru: "Дальше →", uz: "Keyingisi →" });
          next.onclick = () => { i++; render(); };
          quizEl.appendChild(next);
        })
      );
    }
    render();
  }
})();
