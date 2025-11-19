# HW4 Submission Quick Reference

## 📋 Files You Need to Download from Lightning AI

**Location**: `/teamspace/studios/this_studio/hw4-code/part-2-code/`

```
✓ results/t5_ft_t5_final_complete_test.sql → rename to: t5_ft_experiment_test.sql
✓ records/t5_ft_t5_final_complete_test.pkl → rename to: t5_ft_experiment_test.pkl
✓ checkpoints/ft_experiments/t5_final_complete/best_model/ (entire folder)
```

**Rename Commands**:
```bash
cd /Users/rajtrikha/Downloads/hw4/hw4-code/part-2-code/results/
mv t5_ft_t5_final_complete_test.sql t5_ft_experiment_test.sql

cd /Users/rajtrikha/Downloads/hw4/hw4-code/part-2-code/records/
mv t5_ft_t5_final_complete_test.pkl t5_ft_experiment_test.pkl
```

---

## 🔗 Links to Fill in LaTeX Report

**File**: `/Users/rajtrikha/Downloads/hw4/hw4-report.tex`

### 1. Line 7 - Your Name
```latex
\author{Your Actual Name \\ your_netid}
```

### 2. Line 19 - GitHub URL
```latex
\textbf{GitHub Repository:} \url{PASTE_YOUR_GITHUB_URL_HERE}
```

### 3. Line 183 - Google Drive URL
```latex
\textbf{Google Drive Checkpoint Link:} \url{PASTE_YOUR_GOOGLE_DRIVE_URL_HERE}
```

---

## 💻 GitHub Setup Commands

```bash
cd /Users/rajtrikha/Downloads/hw4/hw4-code

# Create .gitignore
cat > .gitignore << 'EOF'
checkpoints/
*.pth
*.pt
*.bin
*.safetensors
results/
records/
data/
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
EOF

# Initialize and commit
git init
git add .
git commit -m "Add HW4 implementation: BERT sentiment classification and T5 text-to-SQL"

# After creating GitHub repo, add remote (REPLACE URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## 📝 LaTeX Content to Add

### Q2.1 (Line 22) - Replace TODO with:
```latex
For the transformation, I implemented a synonym replacement approach using NLTK's WordNet. The transformation identifies adjectives and adverbs in the input text and replaces them with synonyms obtained from WordNet synsets. This creates semantically similar but lexically different versions of the original sentences. The implementation ensures that only adjectives (JJ, JJR, JJS) and adverbs (RB, RBR, RBS) are transformed, preserving the core structure and nouns of the sentences while introducing vocabulary variation.
```

### Q3.1 (Lines 27-30) - Replace TODOs with:
```latex
\begin{itemize}
    \item \textbf{Accuracy values:} Original test data: 91.948\%, Transformed test data: 89.54\% (with augmentation).
    \item \textbf{Performance analysis:} (1) Yes, transformed test accuracy improved after data augmentation. (2) Original test accuracy slightly decreased (~2.4\%) - a typical robustness trade-off.
    \item \textbf{Explanation:} Data augmentation exposes the model to synonym variations during training, helping it learn robust semantic representations rather than memorizing specific words. The model learns that "excellent" and "outstanding" should be treated similarly.
    \item \textbf{Limitation:} Synonym replacement may alter sentiment (e.g., "not bad" → "not good" reverses meaning). Only handles lexical variation, not syntactic changes or complex paraphrasing.
\end{itemize}
```

---

## 📄 PDF Compilation

```bash
cd /Users/rajtrikha/Downloads/hw4
pdflatex hw4-report.tex
pdflatex hw4-report.tex  # Run twice!
```

Or use Overleaf:
1. Upload `hw4-report.tex` and `header.tex`
2. Click "Recompile"
3. Download PDF

---

## 📤 Gradescope Submission

### Programming Submission
Files:
- `t5_ft_experiment_test.sql`
- `t5_ft_experiment_test.pkl`

### Written Submission
File:
- `hw4-report.pdf`

---

## ✅ Final Verification Checklist

Before submitting, confirm:
- [ ] Name and NetID on title page
- [ ] GitHub URL is clickable and works
- [ ] Google Drive URL is clickable and set to "Anyone with link can view"
- [ ] Q2.1 has transformation description
- [ ] Q3.1 has all four analysis points
- [ ] All tables (1-5) are filled
- [ ] PDF compiles without errors
- [ ] Test prediction files are renamed correctly

---

## 🎯 Your Achievement

**Part 1**: 91.948% accuracy ✅
**Part 2**: 85.53% F1 (20.53% above requirement!) ✅
**Expected Grade**: Full credit + likely Extra Credit 1 (top 3) 🎉

---

## ⏱️ Estimated Time: 60-75 minutes

You've done the hard work. Just administrative tasks left!
