# QA Exam CRM Pack (FastAPI + SQLite)

Repository: https://github.com/hryak007-arch/qa-exam-crm-pack

Цей репозиторій містить пакет матеріалів для екзамену з дисципліни **«Забезпечення якості програмних продуктів»** (2–3 відомості) на основі бакалаврського проєкту: **веб-CRM для майстерні ремонту електроніки**.

## 1) Що всередині (структура)
- **bestimt arbeit/** — код мінімальної CRM (FastAPI + SQLite + SQLAlchemy + Pydantic), який використовується для демонстрації тестування
- **tests/** — інтеграційні тести **pytest + FastAPI TestClient** (clients / orders / reports)
- **scripts/** — скрипти підготовки даних:
  - `seed.py` — наповнення тестовими даними
  - `cleanup.py` — очищення/видалення тестових даних (або БД)
- **reports/** — результати SAST:
  - `bandit.txt`
  - `semgrep.txt`
- **requirements.txt** — залежності застосунку
- **requirements-dev.txt** — залежності для тестування/аналізаторів (pytest, pytest-cov, bandit, semgrep)
- **захист.docx** — звіт/матеріали для захисту

> Примітка: назва папки `bestimt arbeit` — робоча (із локального проєкту). Вміст є основним кодом CRM.



