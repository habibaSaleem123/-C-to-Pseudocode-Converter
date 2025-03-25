# AI-Powered C++ to Pseudocode Converter 🚀  

🔍 **Bridging the gap between code and logic!**  
This Transformer-based AI model **translates C++ code into human-readable pseudocode**, making complex logic structures easy to understand.  

---

## 🚀 Key Features  

✅ **AI-Powered Translation** – Converts C++ code into **clear, logical** pseudocode.  
✅ **Transformer-Based Seq2Seq Model** – Understands syntax, loops, and conditions.  
✅ **Interactive Streamlit UI** – Real-time conversion at your fingertips.  
✅ **Handles Large Code Blocks** – Works with **functions, loops, and algorithms**.  
✅ **Enhances Code Understanding** – Ideal for **students, educators, and developers**.  

---

## 🛠 Tech Stack  

- **Python** – Core language  
- **PyTorch** – Deep Learning framework  
- **NLP & Transformers** – Seq2Seq model for code transformation  
- **Streamlit** – Web UI for live testing  
- **C++** – Source code language  

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AbsarRaashid3/CPP2Logic.git  
cd CPP2Logic  
```  

### 2️⃣ Install Dependencies  
Ensure you have **Python 3.8+**, then install required libraries:  
```bash
pip install -r requirements.txt  
```  

---

## 📌 Usage  

### 🔄 **Step 1: Preprocess Data**  
Convert raw training data into paired C++-pseudocode samples:  
```bash
python src/preprocess_code_to_pseudocode.py --input_tsv "data/spoc-train-train.tsv" --output_txt "data/train_pairs_code_to_pseudocode.txt"
```  

### 🏗 **Step 2: Build Vocabulary**  
Generate structured vocabulary for training:  
```bash
python src/vocab.py --pairs_file "data/train_pairs_code_to_pseudocode.txt" --src_vocab_file "src/src_vocab_code2pseudo.pkl" --tgt_vocab_file "src/tgt_vocab_code2pseudo.pkl"
```  

### 🏋️ **Step 3: Train the Model**  
Train the Transformer model on C++-pseudocode pairs:  
```bash
python src/train_code_to_pseudocode.py --pairs_file "data/train_pairs_code_to_pseudocode.txt" --src_vocab_file "src/src_vocab_code2pseudo.pkl" --tgt_vocab_file "src/tgt_vocab_code2pseudo.pkl" --epochs 30 --batch_size 8
```  

### 🔎 **Step 4: Convert C++ to Pseudocode**  
Run inference and translate C++ into human-readable pseudocode:  
```bash
python src/infer_code_to_pseudocode.py --model_checkpoint transformer_code_to_pseudocode.pt --src_vocab_file "src/src_vocab_code2pseudo.pkl" --tgt_vocab_file "src/tgt_vocab_code2pseudo.pkl" --code "int main() { cout << 'Hello World'; }"
```  

---

## 🎨 Web Application  

Launch the **Streamlit UI** for real-time code-to-pseudocode conversion:  
```bash
streamlit run src/app_code_to_pseudocode.py
```  

---

## 🎯 Why Use This?  

💡 **Boosts Learning** – Transforms **complex C++ logic** into easy-to-read pseudocode.  
⚡ **Saves Time** – Automates **manual code explanations**.  
📈 **Improves Algorithm Understanding** – Ideal for **students, researchers, and developers**.  

🚀 **Transform your code into clear logic instantly!**  
