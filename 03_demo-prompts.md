# Demo Prompt Pack / デモ用プロンプト集

The demo uses the dummy files in `sample-data/`. Replace them with his real files once he sends samples.
`sample-data/` のダミーファイルで、事前にリハーサルできます。相手のサンプルが届いたら差し替えてください。

| File | Content |
|---|---|
| `PO-2026-0148.xlsx` | Purchase order (4 beef items, FOB, USD) / 発注書 |
| `Invoice-INV-88231.pdf` | Supplier's commercial invoice / 仕入先の請求書 |
| `PackingList-INV-88231.pdf` | Packing list / パッキングリスト |

**Hidden mistakes in the dummy data (instructor only) / 仕込んだ誤り（講師だけが知っておく）**
1. Short Rib: invoice price **11.85**/kg vs. PO **11.50**/kg（単価の相違）
2. Beef Tongue: **115** cartons shipped vs. **120** ordered（5箱の欠品）
3. Brisket: invoice net weight **6,512.8 kg** vs. packing list **6,498.3 kg**（重量の相違 14.5 kg）

→ Demo 2 で Claude がこの3点を見つけられるか確認します。見つかれば「人が見落としそうなミスを拾える」ことが伝わります。

---

## How to run / 使い方

- **Desktop app:** Attach the files (📎) and paste the prompt.
  デスクトップアプリ：ファイルを添付してプロンプトを貼り付け。
- **Claude Code:** `cd` to the folder that contains the files, run `claude`, and paste the prompt.
  Claude Code：ファイルのあるフォルダで `claude` を起動し、プロンプトを貼り付け。

---

## Demo 1 – PDF → Excel (the "wow" moment) / PDF を Excel に一覧化

**Why / 狙い:** 手入力していた作業がなくなることを、最初の5分で体感してもらう。

```text
Read Invoice-INV-88231.pdf and PackingList-INV-88231.pdf.
Make one Excel file called shipment_INV-88231.xlsx with one row per item.
Columns: item code, description, cartons, net kg (invoice), net kg (packing list),
gross kg, USD/kg, amount USD, production date, best before.
Add a total row. Then tell me the totals in 3 lines.
```

**Check / 確認ポイント:** Excel を開き、合計が PDF と一致するか相手と一緒に確認する（「人がチェックする」習慣づけ）。

---

## Demo 2 – 3-way check (PO vs. invoice vs. packing list) / 3点照合

**Why / 狙い:** 輸入業務で一番価値が伝わりやすい作業。ミスの発見はお金に直結します。

```text
Compare these three documents:
- PO-2026-0148.xlsx (what we ordered)
- Invoice-INV-88231.pdf (what the supplier charges)
- PackingList-INV-88231.pdf (what was shipped)

For each item, check cartons, net weight, unit price, and amount.
List every difference in a table: item, what, PO, invoice, packing list, difference, money impact (USD).
Small weight differences under 0.5% are normal for frozen meat – flag them as "OK" but still show them.
At the end, tell me which differences I should raise with the supplier.
```

**Expected / 期待される結果:** 上の3つの誤りを指摘し、Short Rib の過大請求額（4,986 kg × 0.35 = **USD 1,745.10**）などを計算する。

**Follow-up prompt / 追加の指示:**
```text
Save this check as a reusable checklist file "3way_check_rules.md",
so next time I can just say "run the 3-way check on the new files".
```

---

## Demo 3 – Landed cost per kg / 仕入れ原価の計算

**Why / 狙い:** 毎回 Excel で手計算している原価計算を、条件を変えて試せるようにする。

```text
Using the invoice INV-88231, calculate landed cost per kg for each item.
Assumptions (I will change these later):
- Ocean freight: USD 6,800 per container
- Insurance: 0.3% of invoice value
- Import duty: [X]% of CIF value          <- ask me for the rate
- Customs broker + port + cold storage handling: USD 1,500 per container
- Exchange rate: 1 USD = [Y] (my currency) <- ask me for the rate
Allocate freight and fixed costs by net weight.
Make an Excel file with the assumptions in separate cells so I can edit them,
and use formulas, not fixed numbers.
```

【講師メモ】関税率や為替は国と時期で変わるので、**必ず相手に実際の数字を入れてもらう**こと。Claude に関税率を推測させないでください。

---

## Demo 4 – Supplier email / 仕入先への英文メール

```text
Based on the 3-way check result, draft a polite but firm email to the supplier.
- Ask them to correct the short rib price to USD 11.50/kg as per our PO and reissue the invoice.
- Ask about the 5 missing cartons of beef tongue: backorder or credit note?
- Ask them to confirm the correct net weight for brisket.
Keep it short. Use bullet points. Don't send it – just show me the draft.
```

**Variation / 応用:** "Make a shorter version for WhatsApp."（WhatsApp 用に短く） / "Translate into Japanese / Spanish / Portuguese."

---

## Demo 5 (2nd session) – Make it a routine with Claude Code / 定型作業にする（2回目向け）

Claude Code ならではの使い方：フォルダ単位の一括処理と、手順の保存。

```text
In this folder there is a subfolder "inbox" where I will put new invoices and packing lists every week.
Create a simple routine:
1. Read every new PDF in "inbox".
2. Add the items to "shipment_log.xlsx" (one row per item, keep old rows).
3. Run the 3-way check against the matching PO in "po" folder using 3way_check_rules.md.
4. Write a short summary report "weekly_report.md".
Explain how I run this again next week in one sentence.
```

【講師メモ】ここで `CLAUDE.md`（Claude Code が毎回読むメモ。会社の決まりや用語を書いておく）を一緒に作ると、次回から説明が楽になります：
```text
Create a CLAUDE.md for this folder. Include: what my business does,
our currency, typical suppliers, units (kg, cartons), and the rule
"always ask before changing any existing Excel file".
```

---

## If something goes wrong / うまくいかないとき

| Problem | Say this |
|---|---|
| Result is wrong / 結果が違う | "Row 3 is wrong: the invoice says 4,986.0 kg. Please re-check and fix." |
| Too long / 長すぎる | "Shorter, please. Just the table." |
| Not sure what it did / 何をしたか不明 | "Explain step by step what you did." |
| Scanned PDF unreadable / スキャンPDFが読めない | Try a clearer scan or a photo; ask "What can you read from this file?" |
| It changed a file you didn't want changed / 変えてほしくないファイルを変えた | (Claude Code) Press **Esc**, then "Undo that change." Keep backups of important files. |
