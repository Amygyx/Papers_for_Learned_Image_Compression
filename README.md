# Papers for Neural Image Compression
**Purpose:** We aim to provide a summary of neural image compression. More papers will be summarized.

University of Science and Technology of China (USTC), [Intelligent Media Computing Lab](https://faculty.ustc.edu.cn/chenzhibo).

**📌 About new works.** If you want to incorporate your studies (e.g., the link of paper or project) on neural image compression in this repository. Welcome to raise an issue or email us. We will incorporate it into this repository and our survey report as soon as possible.

## Contents

- [Surveys, Benchmarks & Standards](#surveys-benchmarks--standards)
- [Lossless & Near-lossless Compression](#lossless--near-lossless-compression)
- [Lossy — Distortion-oriented Coding](#lossy--distortion-oriented-coding)
- [Lossy — Perception-oriented Coding](#lossy--perception-oriented-coding)
- [Other tasks](#other-tasks)

## Surveys, Benchmarks & Standards

Surveys, evaluation resources, and standardization milestones for neural image compression.

| Models | Paper | First Author | Venue | Project |
| :--: | :---: | :--: | :--: | :--: |
| -- | [An Overview of the JPEG AI Learning-Based Image Coding Standard](https://doi.org/10.1109/TCSVT.2025.3613244) | S. Esenlik | TCSVT2026 | [link](https://jpeg.org/jpegai/) |
| -- | [A comprehensive survey on image encryption: Taxonomy, challenges, and future directions](https://www.sciencedirect.com/science/article/pii/S0960077923012638) | Morteza SaberiKamarposhti | Chaos, Solitons and Fractals2024 | — |
| -- | [JPEG AI: The First International Standard for Image Coding Based on an End-to-End Learning-Based Approach](https://doi.org/10.1109/MMUL.2024.3485255) | E. Alshina | MultiMedia2024 | [link](https://jpeg.org/jpegai/) |
| -- | [An Introduction to Neural Data Compression](https://www.nowpublishers.com/article/Details/CGV-107) | Yibo Yang | Foundations and Trends in Computer Graphics and Vision2023 | — |
| -- | [Learning-driven lossy image compression: A comprehensive survey](https://doi.org/10.1016/j.engappai.2023.106361) | Sonain Jamil | Engineering Applications of Artificial Intelligence2023 | — |
| -- | [Deep Architectures for Image Compression: A Critical Review](https://doi.org/10.1016/j.sigpro.2021.108346) | Dipti Mishra | Signal Processing2022 | — |
| -- | [Learning End-to-End Lossy Image Compression: A Benchmark](https://arxiv.org/abs/2002.03711) | Yueyu Hu | TPAMI2022 | — |
| -- | [Image and Video Compression With Neural Networks: A Review](https://ieeexplore.ieee.org/document/8693636) | Siwei Ma | TCSVT2019 | — |

## Lossless & Near-lossless Compression



| Models | Paper | First Author | Venue | Project |
| :--: | :---: | :--: | :--: | :--: |
| -- | [Large Language Models for Lossless Image Compression: Next-Pixel Prediction in Language Space is All You Need](https://openreview.net/forum?id=FXBBy1caOX) | Kecheng Chen | NeurIPS2025 | — |
| FNLIC | [Fitted Neural Lossless Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Fitted_Neural_Lossless_Image_Compression_CVPR_2025_paper.html) | Zhe Zhang | CVPR2025 | [![Stars](https://img.shields.io/github/stars/ZZ022/FNLIC.svg?style=social&label=Star)](https://github.com/ZZ022/FNLIC) |
| LosslessINR | [Towards Lossless Implicit Neural Representation via Bit Plane Decomposition](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Towards_Lossless_Implicit_Neural_Representation_via_Bit_Plane_Decomposition_CVPR_2025_paper.html) | Woo Kyoung Han | CVPR2025 | [![Stars](https://img.shields.io/github/stars/WooKyoungHan/LosslessINR.svg?style=social&label=Star)](https://github.com/WooKyoungHan/LosslessINR) |
| -- | [Learned Lossless Image Compression based on Bit Plane Slicing](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learned_Lossless_Image_Compression_based_on_Bit_Plane_Slicing_CVPR_2024_paper.html) | Zhe Zhang | CVPR2024 | — |
| DLPR | [Deep Lossy Plus Residual Coding for Lossless and Near-lossless Image Compression](https://doi.org/10.1109/TPAMI.2023.3348486) | Yuanchao Bai | TPAMI2024 | [![Stars](https://img.shields.io/github/stars/BYchao100/Deep-Lossy-Plus-Residual-Coding.svg?style=social&label=Star)](https://github.com/BYchao100/Deep-Lossy-Plus-Residual-Coding) |
| LC-FDNet | [Learned Lossless Image Compression With Frequency Decomposition Network](https://openaccess.thecvf.com/content/CVPR2022/html/Rhee_LC-FDNet_Learned_Lossless_Image_Compression_With_Frequency_Decomposition_Network_CVPR_2022_paper.html) | Hochang Rhee | CVPR2022 | [![Stars](https://img.shields.io/github/stars/myideaisgood/LC-FDNet.svg?style=social&label=Star)](https://github.com/myideaisgood/LC-FDNet) |
| PILC | [Practical Image Lossless Compression With an End-to-End GPU Oriented Neural Framework](https://openaccess.thecvf.com/content/CVPR2022/html/Kang_PILC_Practical_Image_Lossless_Compression_With_an_End-to-End_GPU_Oriented_CVPR_2022_paper.html) | Ning Kang | CVPR2022 | — |
| iFlow | [iFlow: Numerically Invertible Flows for Efficient Lossless Compression via a Uniform Coder](https://arxiv.org/abs/2111.00965) | Shifeng Zhang | NeurIPS2021 | — |
| OSOA | [OSOA: One-Shot Online Adaptation of Deep Generative Models for Lossless Compression](https://arxiv.org/abs/2111.01662) | Chen Zhang | NeurIPS2021 | — |
| -- | [Improving Lossless Compression Rates via Monte Carlo Bits-Back Coding](https://arxiv.org/abs/2102.11086) | Yangjun Ruan | ICML2021 | [![Stars](https://img.shields.io/github/stars/ryoungj/mcbits.svg?style=social&label=Star)](https://github.com/ryoungj/mcbits) |
| iVPF | [iVPF: Numerical Invertible Volume Preserving Flow for Efficient Lossless Compression](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_iVPF_Numerical_Invertible_Volume_Preserving_Flow_for_Efficient_Lossless_Compression_CVPR_2021_paper.html) | Shifeng Zhang | CVPR2021 | — |
| -- | [Learning Scalable l-infinity-constrained Near-lossless Image Compression via Joint Lossy Image and Residual Compression](https://openaccess.thecvf.com/content/CVPR2021/papers/Bai_Learning_Scalable_lY-Constrained_Near-Lossless_Image_Compression_via_Joint_Lossy_Image_CVPR_2021_paper.pdf) | Yuanchao Bai | CVPR2021 | [![Stars](https://img.shields.io/github/stars/BYchao100/Scalable-Near-lossless-Image-Compression.svg?style=social&label=Star)](https://github.com/BYchao100/Scalable-Near-lossless-Image-Compression) |
| IDF++ | [IDF++: Analyzing and Improving Integer Discrete Flows for Lossless Compression](https://openreview.net/forum?id=MBOyiNnYthd) | Rianne van den Berg | ICLR2021 | — |
| -- | [Ultra High Fidelity Deep Image Decompression With l-infinity-Constrained Compression](https://ieeexplore.ieee.org/document/9277919) | Xi Zhang | TIP2021 | — |
| LBB | [Compression with Flows via Local Bits-Back Coding](https://proceedings.neurips.cc/paper_files/paper/2019/hash/f6e794a75c5d51de081dbefa224304f9-Abstract.html) | Jonathan Ho | NeurIPS2019 | — |
| Bit-Swap | [Bit-Swap: Recursive Bits-Back Coding for Lossless Compression with Hierarchical Latent Variables](https://proceedings.mlr.press/v97/kingma19a.html) | Friso Kingma | ICML2019 | [![Stars](https://img.shields.io/github/stars/fhkingma/bitswap.svg?style=social&label=Star)](https://github.com/fhkingma/bitswap) |
| L3C | [Practical Full Resolution Learned Lossless Image Compression](https://openaccess.thecvf.com/content_CVPR_2019/html/Mentzer_Practical_Full_Resolution_Learned_Lossless_Image_Compression_CVPR_2019_paper.html) | Fabian Mentzer | CVPR2019 | [![Stars](https://img.shields.io/github/stars/fab-jul/L3C-PyTorch.svg?style=social&label=Star)](https://github.com/fab-jul/L3C-PyTorch) |
| BB-ANS | [Practical Lossless Compression with Latent Variables using Bits Back Coding](https://openreview.net/forum?id=ryE98iR5tm) | James Townsend | ICLR2019 | [![Stars](https://img.shields.io/github/stars/bits-back/bits-back.svg?style=social&label=Star)](https://github.com/bits-back/bits-back) |

## Lossy — Distortion-oriented Coding

Methods primarily optimized for rate-distortion performance using pixel-domain fidelity metrics.

| Models | Paper | First Author | Venue | Project |
| :--: | :---: | :--: | :--: | :--: |
| -- | [When the Teacher Has More Bits: Self-Teacher Latent Distillation for Learned Image Compression](https://www.eurecom.fr/en/publication/8851) | Abdellah El Mennaoui | ECCV2026 | — |
| GLIC | [Adaptive Learned Image Compression with Graph Neural Networks](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Adaptive_Learned_Image_Compression_with_Graph_Neural_Networks_CVPR_2026_paper.html) | Yunuo Chen | CVPR2026 | [![Stars](https://img.shields.io/github/stars/UnoC-727/GLIC.svg?style=social&label=Star)](https://github.com/UnoC-727/GLIC) |
| -- | [Learned Image Compression via Sparse Attention and Adaptive Frequency](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Learned_Image_Compression_via_Sparse_Attention_and_Adaptive_Frequency_CVPR_2026_paper.html) | Huidong Ma | CVPR2026 | — |
| CMIC | [Content-Aware Mamba for Learned Image Compression](https://openreview.net/forum?id=WwDNiisZQm) | Yunuo Chen | ICLR2026 | [![Stars](https://img.shields.io/github/stars/UnoC-727/CMIC.svg?style=social&label=Star)](https://github.com/UnoC-727/CMIC) |
| DeepHQ | [DeepHQ: Learned Hierarchical Quantizer for Progressive Deep Image Coding](https://doi.org/10.1145/3773994) | Jooyoung Lee | ACM TOMM2026 | — |
| Cassic | [Cassic: Towards Content-Adaptive State-Space Models for Learned Image Compression](https://openaccess.thecvf.com/content/ICCV2025/html/Qin_Cassic_Towards_Content-Adaptive_State-Space_Models_for_Learned_Image_Compression_ICCV_2025_paper.html) | Shiyu Qin | ICCV2025 | — |
| KDiC | [Knowledge Distillation for Learned Image Compression](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Knowledge_Distillation_for_Learned_Image_Compression_ICCV_2025_paper.html) | Yunuo Chen | ICCV2025 | — |
| HPCM | [Learned Image Compression with Hierarchical Progressive Context Modeling](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Learned_Image_Compression_with_Hierarchical_Progressive_Context_Modeling_ICCV_2025_paper.html) | Yuqi Li | ICCV2025 | [![Stars](https://img.shields.io/github/stars/lyq133/LIC-HPCM.svg?style=social&label=Star)](https://github.com/lyq133/LIC-HPCM) |
| -- | [Balanced Rate-Distortion Optimization in Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Balanced_Rate-Distortion_Optimization_in_Learned_Image_Compression_CVPR_2025_paper.html) | Yichi Zhang | CVPR2025 | [link](https://gitlab.com/viper-purdue/Balanced-RD) |
| DCAE | [Learned Image Compression with Dictionary-based Entropy Model](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Learned_Image_Compression_with_Dictionary-based_Entropy_Model_CVPR_2025_paper.html) | Jingbo Lu | CVPR2025 | [![Stars](https://img.shields.io/github/stars/LabShuHangGU/DCAE.svg?style=social&label=Star)](https://github.com/LabShuHangGU/DCAE) |
| LALIC | [Linear Attention Modeling for Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_Linear_Attention_Modeling_for_Learned_Image_Compression_CVPR_2025_paper.html) | Donghui Feng | CVPR2025 | [![Stars](https://img.shields.io/github/stars/sjtu-medialab/RwkvCompress.svg?style=social&label=Star)](https://github.com/sjtu-medialab/RwkvCompress) |
| ALVQ | [Multirate Neural Image Compression with Adaptive Lattice Vector Quantization](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Multirate_Neural_Image_Compression_with_Adaptive_Lattice_Vector_Quantization_CVPR_2025_paper.html) | Hao Xu | CVPR2025 | — |
| -- | [Test-time Adaptation for Image Compression with Distribution Regularization](https://openreview.net/forum?id=bsnRUkVn63) | Kecheng Chen | ICLR2025 | — |
| -- | [Efficient Progressive Image Compression with Variance-Aware Masking](https://openaccess.thecvf.com/content/WACV2025/html/Presta_Efficient_Progressive_Image_Compression_with_Variance-Aware_Masking_WACV_2025_paper.html) | Elena Presta | WACV2025 | — |
| -- | [Few-Shot Domain Adaptation for Learned Image Compression](https://doi.org/10.1609/aaai.v39i10.33100) | Tianyu Zhang | AAAI2025 | — |
| CCA | [Causal Context Adjustment Loss for Learned Image Compression](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f074a994e062146561db9cdc63999efa-Abstract-Conference.html) | Minghao Han | NeurIPS2024 | — |
| OLVQ | [Learning Optimal Lattice Vector Quantizers for End-to-End Neural Image Compression](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c09916f6f0c428a97a09a53648e5002e-Abstract-Conference.html) | Xi Zhang | NeurIPS2024 | — |
| SGA+ | [Robustly Overfitting Latents for Flexible Neural Image Compression](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c1233cb30ef11a3fe6ab10aa96beabaf-Abstract-Conference.html) | Yura Perugachi-Diaz | NeurIPS2024 | — |
| WCLIC | [Window-based Channel Attention for Wavelet-enhanced Learned Image Compression](https://openaccess.thecvf.com/content/ACCV2024/html/Xu_Window-based_Channel_Attention_for_Wavelet-enhanced_Learned_Image_Compression_ACCV_2024_paper.html) | Heng Xu | ACCV2024 | — |
| BaSIC | [BaSIC: BayesNet Structure Learning for Computational Scalable Neural Image Compression](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03640.pdf) | Yufeng Zhang | ECCV2024 | [![Stars](https://img.shields.io/github/stars/worldlife123/cbench_BaSIC.svg?style=social&label=Star)](https://github.com/worldlife123/cbench_BaSIC) |
| SegPIC | [Region-Adaptive Transform with Segmentation Prior for Image Compression](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6270_ECCV_2024_paper.php) | Yuxi Liu | ECCV2024 | [![Stars](https://img.shields.io/github/stars/GityuxiLiu/SegPIC-for-Image-Compression.svg?style=social&label=Star)](https://github.com/GityuxiLiu/SegPIC-for-Image-Compression) |
| WeConvene | [WeConvene: Learned Image Compression with Wavelet-Domain Convolution and Entropy Model](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06635.pdf) | Haisheng Fu | ECCV2024 | — |
| -- | [Towards Backward-Compatible Continual Learning of Image Compression](https://openaccess.thecvf.com/content/CVPR2024/html/Duan_Towards_Backward-Compatible_Continual_Learning_of_Image_Compression_CVPR_2024_paper.html) | Zhihao Duan | CVPR2024 | [link](https://gitlab.com/viper-purdue/continual-compression) |
| -- | [Towards Efficient Image Compression Without Autoregressive Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/170dc3e41f2d03e327e04dbab0fccbfb-Abstract-Conference.html) | Muhammad Salman Ali | NeurIPS2023 | — |
| TCM | [Learned Image Compression with Mixed Transformer-CNN Architectures](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_Learned_Image_Compression_With_Mixed_Transformer-CNN_Architectures_CVPR_2023_paper.html) | Jinming Liu | CVPR2023 | [![Stars](https://img.shields.io/github/stars/jmliu206/LIC_TCM.svg?style=social&label=Star)](https://github.com/jmliu206/LIC_TCM) |
| NVTC | [NVTC: Nonlinear Vector Transform Coding](https://openaccess.thecvf.com/content/CVPR2023/html/Feng_NVTC_Nonlinear_Vector_Transform_Coding_CVPR_2023_paper.html) | Runsen Feng | CVPR2023 | [![Stars](https://img.shields.io/github/stars/USTC-IMCL/NVTC.svg?style=social&label=Star)](https://github.com/USTC-IMCL/NVTC) |
| -- | [Content-Oriented Learned Image Compression](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/7542_ECCV_2022_paper.php) | Meng Li | ECCV2022 | — |
| Contextformer | [Contextformer: A Transformer with Spatio-Channel Attention for Context Modeling in Learned Image Compression](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6046_ECCV_2022_paper.php) | Ahmet Burakhan Koyuncu | ECCV2022 | — |
| ELIC | [ELIC: Efficient Learned Image Compression with Unevenly Grouped Space-Channel Contextual Adaptive Coding](https://openaccess.thecvf.com/content/CVPR2022/html/He_ELIC_Efficient_Learned_Image_Compression_With_Unevenly_Grouped_Space-Channel_Contextual_CVPR_2022_paper.html) | Dailan He | CVPR2022 | — |
| -- | [The Devil Is in the Details: Window-Based Attention for Image Compression](https://openaccess.thecvf.com/content/CVPR2022/html/Zou_The_Devil_Is_in_the_Details_Window-Based_Attention_for_Image_CVPR_2022_paper.html) | Renjie Zou | CVPR2022 | [![Stars](https://img.shields.io/github/stars/Googolxx/STF.svg?style=social&label=Star)](https://github.com/Googolxx/STF) |
| CCP | [Causal Contextual Prediction for Learned Image Compression](https://doi.org/10.1109/TCSVT.2021.3089491) | Zongyu Guo | TCSVT2022 | — |
| -- | [Soft Then Hard: Rethinking the Quantization in Neural Image Compression](https://proceedings.mlr.press/v139/guo21c.html) | Zongyu Guo | ICML2021 | — |
| -- | [Checkerboard Context Model for Efficient Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2021/html/He_Checkerboard_Context_Model_for_Efficient_Learned_Image_Compression_CVPR_2021_paper.html) | Dailan He | CVPR2021 | — |
| -- | [Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules](https://openaccess.thecvf.com/content_CVPR_2020/html/Cheng_Learned_Image_Compression_With_Discretized_Gaussian_Mixture_Likelihoods_and_Attention_CVPR_2020_paper.html) | Zhengxue Cheng | CVPR2020 | — |
| -- | [Coarse-to-Fine Hyper-Prior Modeling for Learned Image Compression](https://doi.org/10.1609/aaai.v34i07.6736) | Yueyu Hu | AAAI2020 | — |
| -- | [Joint Autoregressive and Hierarchical Priors for Learned Image Compression](https://proceedings.neurips.cc/paper/2018/hash/53edebc543333dfbf7c5933af792c9c4-Abstract.html) | David Minnen | NeurIPS2018 | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| -- | [Variational Image Compression with a Scale Hyperprior](https://openreview.net/forum?id=rkcQFMZRb) | Johannes Balle | ICLR2018 | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| -- | [Soft-to-Hard Vector Quantization for End-to-End Learning Compressible Representations](https://proceedings.neurips.cc/paper/2017/hash/86b122d4358357d834a87ce618a55de0-Abstract.html) | Eirikur Agustsson | NeurIPS2017 | — |
| -- | [End-to-end Optimized Image Compression](https://openreview.net/forum?id=rJxdQ3jeg) | Johannes Balle | ICLR2017 | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| -- | [Lossy Image Compression with Compressive Autoencoders](https://openreview.net/forum?id=rJiNwv9gg) | Lucas Theis | ICLR2017 | — |

## Lossy — Perception-oriented Coding

Methods primarily optimized for perceptual quality or the rate-distortion-perception trade-off.

| Models | Paper | First Author | Venue | Project |
| :--: | :---: | :--: | :--: | :--: |
| NeFIC | [Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors](https://arxiv.org/abs/2603.15129) | Yunuo Chen | ECCV2026 | [![Stars](https://img.shields.io/github/stars/UnoC-727/NeFIC.svg?style=social&label=Star)](https://github.com/UnoC-727/NeFIC) |
| CoD-Lite | [CoD-Lite: Real-Time Diffusion-Based Generative Image Compression](https://icml.cc/virtual/2026/poster/63715) | Zhaoyang Jia | ICML2026 | [![Stars](https://img.shields.io/github/stars/microsoft/GenCodec.svg?style=social&label=Star)](https://github.com/microsoft/GenCodec/tree/main/CoD_Lite) |
| CADC | [CADC: Content Adaptive Diffusion-Based Generative Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_CADC_Content_Adaptive_Diffusion-Based_Generative_Image_Compression_CVPR_2026_paper.html) | Xihua Sheng | CVPR2026 | — |
| CoD | [CoD: A Diffusion Foundation Model for Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Jia_CoD_A_Diffusion_Foundation_Model_for_Image_Compression_CVPR_2026_paper.html) | Zhaoyang Jia | CVPR2026 | [![Stars](https://img.shields.io/github/stars/microsoft/GenCodec.svg?style=social&label=Star)](https://github.com/microsoft/GenCodec/tree/main/CoD) |
| DiT-IC | [DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_DiT-IC_Aligned_Diffusion_Transformer_for_Efficient_Image_Compression_CVPR_2026_paper.html) | Junqi Shi | CVPR2026 | — |
| -- | [Ultra-Low Bitrate Perceptual Image Compression with Shallow Encoder](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Ultra-Low_Bitrate_Perceptual_Image_Compression_with_Shallow_Encoder_CVPR_2026_paper.html) | Tianyu Zhang | CVPR2026 | — |
| -- | [What Matters in Practical Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Tatwawadi_What_Matters_in_Practical_Learned_Image_Compression_CVPR_2026_paper.html) | Kedar Tatwawadi | CVPR2026 | — |
| Turbo-DDCM | [Turbo-DDCM: Fast and Flexible Zero-Shot Diffusion-Based Image Compression](https://openreview.net/forum?id=eIF1QvC94Z) | Amit Vaisman | ICLR2026 | — |
| OneDC | [One-Step Diffusion-Based Image Compression with Semantic Distillation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/352a67c085e607acdcfc0076899750f4-Abstract-Conference.html) | Naifu Xue | NeurIPS2025 | [link](https://onedc-codec.github.io/) |
| OSCAR | [OSCAR: One-Step Diffusion Codec Across Multiple Bit-rates](https://openreview.net/forum?id=uodE9CAXaF) | Jinpei Guo | NeurIPS2025 | [![Stars](https://img.shields.io/github/stars/jp-guo/OSCAR.svg?style=social&label=Star)](https://github.com/jp-guo/OSCAR) |
| StableCodec | [StableCodec: Taming One-Step Diffusion for Extreme Image Compression](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_StableCodec_Taming_One-Step_Diffusion_for_Extreme_Image_Compression_ICCV_2025_paper.pdf) | Tianyu Zhang | ICCV2025 | [![Stars](https://img.shields.io/github/stars/LuizScarlet/StableCodec.svg?style=social&label=Star)](https://github.com/LuizScarlet/StableCodec) |
| DDCM | [Compressed Image Generation with Denoising Diffusion Codebook Models](https://icml.cc/virtual/2025/poster/44687) | Guy Ohayon | ICML2025 | [![Stars](https://img.shields.io/github/stars/DDCM-2025/ddcm-compressed-image-generation.svg?style=social&label=Star)](https://github.com/DDCM-2025/ddcm-compressed-image-generation) |
| -- | [Bridging the Gap between Gaussian Diffusion Models and Universal Quantization for Image Compression](https://openaccess.thecvf.com/content/CVPR2025/papers/Relic_Bridging_the_Gap_between_Gaussian_Diffusion_Models_and_Universal_Quantization_CVPR_2025_paper.pdf) | Lucas Relic | CVPR2025 | — |
| -- | [Decouple Distortion from Perception: Region Adaptive Diffusion for Extreme-low Bitrate Perception Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Decouple_Distortion_from_Perception_Region_Adaptive_Diffusion_for_Extreme-low_Bitrate_CVPR_2025_paper.html) | Jinchang Xu | CVPR2025 | — |
| -- | [Good, Cheap, and Fast: Overfitted Image Compression with Wasserstein Distortion](https://openaccess.thecvf.com/content/CVPR2025/html/Balle_Good_Cheap_and_Fast_Overfitted_Image_Compression_with_Wasserstein_Distortion_CVPR_2025_paper.html) | Jona Balle | CVPR2025 | — |
| DiffC | [Lossy Compression with Pretrained Diffusion Models](https://openreview.net/forum?id=raUnLe0Z04) | Jeremy Vonderfecht | ICLR2025 | [![Stars](https://img.shields.io/github/stars/JeremyIV/diffc.svg?style=social&label=Star)](https://github.com/JeremyIV/diffc) |
| DiffEIC | [Towards Extreme Image Compression with Latent Feature Guidance and Diffusion Prior](https://doi.org/10.1109/TCSVT.2024.3455576) | Zhiyuan Li | TCSVT2025 | [![Stars](https://img.shields.io/github/stars/huai-chang/DiffEIC.svg?style=social&label=Star)](https://github.com/huai-chang/DiffEIC) |
| -- | [Lossy Image Compression with Foundation Diffusion Models](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7844_ECCV_2024_paper.php) | Lucas Relic | ECCV2024 | — |
| TACO | [Neural Image Compression with Text-guided Encoding for both Pixel-level and Perceptual Fidelity](https://taco-nic.github.io/) | Hagyeong Lee | ICML2024 | [link](https://taco-nic.github.io/) |
| GLC | [Generative Latent Coding for Ultra-Low Bitrate Image Compression](https://openaccess.thecvf.com/content/CVPR2024/html/Jia_Generative_Latent_Coding_for_Ultra-Low_Bitrate_Image_Compression_CVPR_2024_paper.html) | Zhaoyang Jia | CVPR2024 | [![Stars](https://img.shields.io/github/stars/jzyustc/GLC.svg?style=social&label=Star)](https://github.com/jzyustc/GLC) |
| -- | [Idempotence and Perceptual Image Compression](https://openreview.net/forum?id=Cy5v64DqEF) | Tongda Xu | ICLR2024 | [![Stars](https://img.shields.io/github/stars/tongdaxu/Idempotence-and-Perceptual-Image-Compression.svg?style=social&label=Star)](https://github.com/tongdaxu/Idempotence-and-Perceptual-Image-Compression) |
| PerCo | [Towards Image Compression with Perfect Realism at Ultra-Low Bitrates](https://openreview.net/forum?id=ktdETU9JBg) | Marlene Careil | ICLR2024 | — |
| CDC | [Lossy Image Compression with Conditional Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ccf6d8b4a1fe9d9c8192f00c713872ea-Abstract-Conference.html) | Ruihan Yang | NeurIPS2023 | [![Stars](https://img.shields.io/github/stars/buggyyang/CDC_compression.svg?style=social&label=Star)](https://github.com/buggyyang/CDC_compression) |
| MS-ILLM | [Improving Statistical Fidelity for Neural Image Compression with Implicit Local Likelihood Models](https://icml.cc/virtual/2023/poster/24565) | Matthew Muckley | ICML2023 | [![Stars](https://img.shields.io/github/stars/facebookresearch/NeuralCompression.svg?style=social&label=Star)](https://github.com/facebookresearch/NeuralCompression) |
| HiFiC | [High-Fidelity Generative Image Compression](https://proceedings.neurips.cc/paper/2020/hash/8a50bae297807da9e97722a0b3fd8f27-Abstract.html) | Fabian Mentzer | NeurIPS2020 | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression/tree/master/models/hific) |
| -- | [Generative Adversarial Networks for Extreme Learned Image Compression](https://openaccess.thecvf.com/content_ICCV_2019/html/Agustsson_Generative_Adversarial_Networks_for_Extreme_Learned_Image_Compression_ICCV_2019_paper.html) | Eirikur Agustsson | ICCV2019 | — |
| -- | [Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff](https://proceedings.mlr.press/v97/blau19a.html) | Yochai Blau | ICML2019 | — |

## Other tasks

### Encryption

| Methods | Paper | First Author | Venue |
| :--: | :---: | :--: | :--: |
| Visual Cryptography | [Dynamic feedback bit-level image privacy protection based on chaos and information hiding](https://www.nature.com/articles/s41598-024-53325-4) | Jinlong Zhang | scientific Reports, 2024 |
| CS | [A multi-level privacy-preserving scheme for extracting traffic images](https://www.sciencedirect.com/science/article/pii/S0165168424000641) | Xiaofei He | Signal Processing, 2024 |
| DNA | [A novel image compression and encryption scheme based on conservative chaotic system and DNA method](https://www.sciencedirect.com/science/article/pii/S0960077923003934?via%3Dihub) | Xin Wu | Chaos, Solitons and Fractals, 2023 |
