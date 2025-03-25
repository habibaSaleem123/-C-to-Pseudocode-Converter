# src/app_code_to_pseudocode.py

import streamlit as st
import torch
import pickle
from model import TransformerSeq2Seq
from vocab import Vocabulary, SPECIAL_TOKENS
from infer_code_to_pseudocode import greedy_decode

@st.cache_resource
def load_model_and_vocab():
    with open("src/src_vocab_code2pseudo.pkl", "rb") as f:
        src_vocab = pickle.load(f)
    with open("src/tgt_vocab_code2pseudo.pkl", "rb") as f:
        tgt_vocab = pickle.load(f)
    model = TransformerSeq2Seq(
        src_vocab_size=len(src_vocab),
        tgt_vocab_size=len(tgt_vocab),
        d_model=256,
        n_heads=4,
        d_ff=512,
        num_layers=2
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.load_state_dict(torch.load("transformer_code_to_pseudocode.pt", map_location=device))
    model.to(device)
    model.eval()
    return model, src_vocab, tgt_vocab, device

def main():
    st.title("CPP2Logic")
    st.write("Enter your C++ code below:")

    code_input = st.text_area("C++ Code", height=200)
    if st.button("Convert to Pseudocode"):
        if code_input.strip():
            model, src_vocab, tgt_vocab, device = load_model_and_vocab()
            tokens = code_input.split()
            src_ids = [src_vocab.word2idx.get(token, src_vocab.word2idx["<unk>"]) for token in tokens]
            output_ids = greedy_decode(model, src_ids, src_vocab, tgt_vocab, device=device)
            output_tokens = [tgt_vocab.idx2word[i] for i in output_ids]
            filtered_tokens = [token for token in output_tokens if token not in SPECIAL_TOKENS]
            st.code(" ".join(filtered_tokens), language="text")
        else:
            st.warning("Please enter some C++ code!")

if __name__ == "__main__":
    main()
