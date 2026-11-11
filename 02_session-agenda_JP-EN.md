# Claude Session – Agenda & Cheat Sheet / 当日アジェンダ & 早見表

> 講師（あなた）用メモは **【講師メモ】** で書いています。相手に送るときはその部分を消してもOKです。
> Lines marked **【講師メモ】** are notes for the instructor.

---

## Part A. Setup call (15 min, a few days before) / 事前セットアップ通話

**Goal / 目的:** Claude works on your computer before the main session.
本番前に、相手のPCで Claude が動く状態にしておく。

| Step | English | 日本語 |
|---|---|---|
| 1 | Sign up at **claude.ai** and choose the **Pro** plan (or higher). | claude.ai でアカウント作成、Pro 以上を契約 |
| 2 | Install the **Claude desktop app** (claude.ai/download). | Claude デスクトップアプリをインストール |
| 3 | *(Option)* Install **Claude Code** – see commands below. | （任意）Claude Code をインストール |
| 4 | Make a folder: `Documents/claude-work` and put the sample files there. | 作業用フォルダを作り、サンプルを入れる |
| 5 | Test: ask Claude "Hello, can you see the files in this folder?" | 動作確認 |

**Claude Code install (official native installer) / インストールコマンド**

- Mac (Terminal):
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- Windows (PowerShell):
  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```
- Then / その後:
  ```bash
  cd ~/Documents/claude-work
  claude
  ```
  → A browser opens for login. / ブラウザが開くのでログイン。

【講師メモ】
- インストール手順は変わることがあります。前日に公式ドキュメント（code.claude.com/docs）で最新の手順を確認してください。
- ヒアリングシートの Q10 が「Never（ターミナルを使ったことがない）」なら、**本番はデスクトップアプリで進め**、Claude Code は2回目に回すのが無難です。
- 相手側の画面を操作するなら、Zoom の「リモート制御」機能を事前に許可してもらうとスムーズです。

---

## Part B. Main session (60–90 min) / 本番

| Time | Section | What happens / 内容 |
|---|---|---|
| 0:00 | **Intro** (10 min) | What Claude is / Claude とは何か（下の「3 key ideas」） |
| 0:10 | **Demo** (15 min) | Instructor shares screen and solves one problem with *his* files / 講師が画面共有し、相手のファイルで1つ解決 |
| 0:25 | **Hands-on** (30 min) | He shares screen and types the prompts himself / 相手が画面共有し、自分で指示を入力 |
| 0:55 | **Next step** (10 min) | Save good prompts, pick 1 homework task / 良かった指示文を保存し、宿題を1つ決める |
| 1:05 | Buffer / Q&A | 予備時間 |

【講師メモ】
- 説明は短く。**10分以内に「動くところ」を見せる**のが鉄則です。
- デモは `03_demo-prompts.md` の **Demo 1 → 2** の順に進めます（PDF を Excel 化 → 書類の突き合わせ）。どちらも効果が分かりやすいです。
- 実習では**相手に自分でキーボードを打ってもらう**。講師が代わりに打つと定着しません。
- 相手の言葉で頼んでもらう（英語でOK）。うまく伝わらなければ「もう一度、具体的に」と促します。

---

## Part C. Intro – 3 key ideas / 冒頭で伝える3つのこと

1. **Talk to it like a smart assistant – in plain English.**
   普通の英語（日本語でも可）で、アシスタントに頼むように話せばいい。

2. **Give it your files, tell it the goal, check the result.**
   ファイルを渡す → ゴールを伝える → 結果をチェックする。

3. **You are the boss. Always check numbers.**
   最終確認は人間の仕事。金額・重量は必ず確認する。

---

## Part D. Cheat Sheet (give this to him) / 早見表（相手に渡す用）

### How to ask / 頼み方のコツ

| Tip | Example |
|---|---|
| **Say the goal** / ゴールを言う | "I want one Excel table of all items in these invoices." |
| **Say the format** / 形式を言う | "Columns: item, cartons, net kg, USD/kg, amount." |
| **Point to the files** / ファイルを指定 | "Use Invoice-INV-88231.pdf and PO-2026-0148.xlsx." |
| **Ask it to check** / 確認させる | "Double-check the totals and tell me if anything looks wrong." |
| **Ask it to ask you** / 質問させる | "If anything is unclear, ask me before you start." |
| **Iterate** / 直させる | "Good. Now add a column for landed cost per kg." |

### Useful phrases / 使えるフレーズ

- "Read all PDFs in this folder and…"
- "Compare A and B and list every difference."
- "Make it an Excel file I can open."
- "Explain what you did in simple words."
- "Save this as a reusable checklist / template."
- "Draft a polite email to the supplier about this."

### Claude Code basics (if using the terminal) / Claude Code の基本

| Action | How |
|---|---|
| Start / 起動 | Open Terminal → `cd` to your work folder → type `claude` |
| Stop a task / 途中で止める | Press **Esc** |
| Clear the conversation / 会話をリセット | type `/clear` |
| Exit / 終了 | type `/exit` or press **Ctrl + C** twice |
| Permission prompts / 許可の確認 | Claude asks before changing files. Read, then choose **Yes** or **No**. |

### Safety / 注意

- Check prices, weights, and totals yourself before you send or pay anything.
  金額・重量・合計は送信や支払いの前に必ず自分で確認する。
- Follow your company's data rules. Use dummy data when unsure.
  社内ルールに従う。迷ったらダミーデータを使う。
- Claude drafts emails – **you** press send.
  メールは下書きまで。送信ボタンは人が押す。

---

## Part E. Homework & follow-up / 宿題とフォロー

- [ ] Use the saved prompt on **one real task** this week. / 今週、保存した指示文を実際の仕事で1回使う
- [ ] Write down: time before vs. after. / かかった時間を Before / After で記録する
- [ ] Note any problems or questions. / うまくいかなかった点をメモする
- [ ] Follow-up call (30 min) in 1–2 weeks. / 1〜2週間後に30分のフォロー通話

【講師メモ】2回目の候補：仕入れ原価の計算（Demo 3）、英文メールの下書き（Demo 4）、Claude Code で「毎回同じ作業」を1コマンドで実行できるようにする（Demo 5）。
