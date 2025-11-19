# HW4 Part 2 - Final Submission Checklist

## ✅ Completed

- [x] Part 1 Q1-Q3 (already done)
- [x] Part 2 training (85.53% F1 achieved!)
- [x] Q4: Data statistics tables (Table 1 & 2)
- [x] Q5: T5 fine-tuning details (Table 3)
- [x] Q6: Results and error analysis (Tables 4 & 5)
- [x] LaTeX report template filled out

---

## 📋 Remaining Tasks

### 1. Download Files from Lightning AI

**Files to download:**
```
/teamspace/studios/this_studio/hw4-code/part-2-code/results/t5_ft_t5_final_complete_test.sql
/teamspace/studios/this_studio/hw4-code/part-2-code/records/t5_ft_t5_final_complete_test.pkl
/teamspace/studios/this_studio/hw4-code/part-2-code/checkpoints/ft_experiments/t5_final_complete/best_model/
```

**How to download from Lightning AI:**
- Option 1: Use Lightning AI interface to download files
- Option 2: Use terminal commands if you have access:
  ```bash
  # Zip the checkpoint folder first
  cd /teamspace/studios/this_studio/hw4-code/part-2-code/checkpoints/ft_experiments/t5_final_complete
  tar -czf best_model.tar.gz best_model/
  ```

### 2. Rename Test Prediction Files

Once downloaded, rename:
```bash
mv t5_ft_t5_final_complete_test.sql t5_ft_experiment_test.sql
mv t5_ft_t5_final_complete_test.pkl t5_ft_experiment_test.pkl
```

### 3. Create GitHub Repository

**Steps:**
1. Create new GitHub repo (e.g., "nlp-hw4" or "text-to-sql-t5")
2. Upload all code:
   ```
   part-1-code/
   ├── main.py
   ├── utils.py
   └── requirements.txt

   part-2-code/
   ├── load_data.py
   ├── train_t5.py
   ├── t5_utils.py
   ├── utils.py
   ├── evaluate.py
   └── data/ (optional - can reference it's provided)
   ```
3. Add README.md explaining:
   - How to run training
   - Dependencies
   - Results achieved
4. Copy the GitHub URL

**Example README structure:**
```markdown
# HW4: Fine-tuning Language Models

## Part 1: BERT Sentiment Classification
- Accuracy achieved: [your result]

## Part 2: T5 Text-to-SQL
- Dev F1: 85.53%
- Test F1: 85.53%

## Setup
[installation instructions]

## Training
[how to run]
```

### 4. Upload Checkpoint to Google Drive

**Steps:**
1. Upload the `best_model` folder (or `best_model.tar.gz`) to your Google Drive
2. Right-click → "Get link" → "Anyone with the link can view"
3. Copy the shareable link
4. The folder should contain:
   ```
   best_model/
   ├── config.json
   ├── generation_config.json
   └── model.safetensors
   ```

### 5. Update LaTeX Report

**File:** `/Users/rajtrikha/Downloads/hw4/hw4-report.tex`

**Fill in placeholders:**
1. Line ~7: Replace "Full Name \\ Net ID" with your actual info
2. Line ~19: Replace `[TO BE ADDED - create repo and paste link here]` with your GitHub URL
3. Line ~183: Replace `[TO BE ADDED - upload best_model folder and paste shareable link here]` with your Google Drive link

**Part 1 sections to fill (if not done):**
- Q2.1: Your transformation description
- Q3.1: Your augmentation analysis

### 6. Compile PDF

**On your local machine:**
```bash
cd /Users/rajtrikha/Downloads/hw4
pdflatex hw4-report.tex
pdflatex hw4-report.tex  # Run twice to resolve references
```

Or use Overleaf:
1. Upload hw4-report.tex and header.tex to Overleaf
2. Compile
3. Download PDF

### 7. Submit to Gradescope

**Programming submission:**
- [x] Part 1: out_original.txt, out_transformed.txt, out_augmented_original.txt, out_augmented_transformed.txt
- [ ] Part 2: t5_ft_experiment_test.sql, t5_ft_experiment_test.pkl

**Written submission:**
- [ ] hw4-report.pdf (with GitHub and Google Drive links!)

---

## 🎯 Final Checklist Before Submit

- [ ] Downloaded all files from Lightning AI
- [ ] Renamed test prediction files correctly
- [ ] Created GitHub repository with all code
- [ ] Uploaded checkpoint to Google Drive
- [ ] Updated LaTeX with both links (GitHub + Drive)
- [ ] Compiled PDF successfully
- [ ] PDF includes ALL required content:
  - [ ] Q0: GitHub link
  - [ ] Q2: Transformation description (Part 1)
  - [ ] Q3: Augmentation analysis (Part 1)
  - [ ] Q4: Tables 1 & 2 (filled)
  - [ ] Q5: Table 3 (filled)
  - [ ] Q6: Tables 4 & 5 (filled)
  - [ ] Q7: Google Drive link
- [ ] Submitted test files to Gradescope programming
- [ ] Submitted PDF to Gradescope written

---

## 🏆 Expected Scores

**Part 2 Performance Grading:**
- Your F1: 85.53%
- Requirement: ≥65 F1
- **Score: 25/25 points** ✅ (full credit!)

**Part 2 Written Grading:**
- Q4 (5pts): Tables complete ✅
- Q5 (10pts): Detailed implementation description ✅
- Q6 (10pts): Results + 3 error types analyzed ✅
- **Score: 25/25 points** ✅

**Total Part 2: 50/50 points expected** 🎉

---

## 📝 Notes

- Make sure Google Drive link is set to "Anyone with the link can view"
- GitHub repo can be private or public (both are fine)
- Test predictions should be generated from the best checkpoint (epoch 24)
- Don't submit excessively to Gradescope test set (they may deduct points)

---

## 🆘 If You Need Help

**Common Issues:**

1. **LaTeX won't compile**
   - Make sure `header.tex` is in the same directory
   - Check for missing packages (booktabs, pdflscape, etc.)
   - Use Overleaf if local compilation fails

2. **Can't download from Lightning AI**
   - Try zipping files first
   - Use Lightning AI's download feature in the UI
   - Can recreate test predictions locally if needed

3. **GitHub upload too large**
   - Don't include checkpoints in GitHub (only Google Drive)
   - Don't include data folder (it's provided)
   - Use .gitignore for large files

4. **Google Drive link not working**
   - Make sure sharing is set to "Anyone with the link"
   - Test the link in an incognito window
   - Direct link to folder should work

---

## ⏱️ Time Estimate

- Downloading files: 10-15 min
- GitHub setup: 15-20 min
- Google Drive upload: 10-15 min
- PDF compilation: 5-10 min
- **Total: ~1 hour**

Good luck! 🚀
