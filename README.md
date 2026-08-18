# Papers for Neural Image Compression
**Purpose:** We aim to provide a summary of neural image compression. More papers will be summarized.

University of Science and Technology of China (USTC), [Intelligent Media Computing Lab](https://faculty.ustc.edu.cn/chenzhibo).

**📌 About new works.** If you want to incorporate your studies (e.g., the link of paper or project) on neural image compression in this repository. Welcome to raise an issue or email us. We will incorporate it into this repository and our survey report as soon as possible.

<!-- Paper tables below are generated from data/papers.yml. -->
**Last curated:** 2026-08-18  
**Coverage:** 63 selected publications and preprints.

This first curation pass focuses on surveys and standards, lossless/near-lossless coding, distortion-oriented lossy coding, and perception-oriented lossy coding. Semantic or human-machine coding, special image domains, and broader visual compression are currently [deferred](DEFERRED.md).

## Contents

- [Surveys, Benchmarks & Standards](#surveys-benchmarks-standards)
- [Lossless & Near-lossless Compression](#lossless-near-lossless-compression)
- [Lossy — Distortion-oriented Coding](#lossy-distortion-oriented-coding)
- [Lossy — Perception-oriented Coding](#lossy-perception-oriented-coding)

## Tag vocabulary

- **Objective:** `lossless`, `near-lossless`, `distortion`, `perception`
- **Paradigm:** `transform`, `flow`, `vq`, `inr`, `overfitted`, `gan`, `diffusion`, `foundation-model`
- **Focus:** `transform`, `entropy-model`, `quantization`, `optimization`, `adaptation`
- **Capability:** `variable-rate`, `progressive`, `scalable`, `content-adaptive`, `low-complexity`, `practical`

## Surveys, Benchmarks & Standards

Surveys, evaluation resources, and standardization milestones for neural image compression.

| Year | Paper | First author | Venue | Tags | Code / project |
| :--: | --- | --- | --- | --- | :--: |
| 2026 | [An Overview of the JPEG AI Learning-Based Image Coding Standard](https://doi.org/10.1109/TCSVT.2025.3613244) | S. Esenlik | IEEE TCSVT | `transform` · `standardization` · `practical` | [link](https://jpeg.org/jpegai/) |
| 2024 | [A comprehensive survey on image encryption: Taxonomy, challenges, and future directions](https://www.sciencedirect.com/science/article/pii/S0960077923012638) | Morteza SaberiKamarposhti | Chaos, Solitons and Fractals |  | — |
| 2024 | [JPEG AI: The First International Standard for Image Coding Based on an End-to-End Learning-Based Approach](https://doi.org/10.1109/MMUL.2024.3485255) | E. Alshina | IEEE MultiMedia | `transform` · `standardization` · `practical` | [link](https://jpeg.org/jpegai/) |
| 2023 | [An Introduction to Neural Data Compression](https://www.nowpublishers.com/article/Details/CGV-107) | Yibo Yang | Foundations and Trends in Computer Graphics and Vision | `transform` · `benchmark` | — |
| 2023 | [Learning-driven lossy image compression: A comprehensive survey](https://doi.org/10.1016/j.engappai.2023.106361) | Sonain Jamil | Engineering Applications of Artificial Intelligence | `transform` · `benchmark` | — |
| 2022 | [Deep Architectures for Image Compression: A Critical Review](https://doi.org/10.1016/j.sigpro.2021.108346) | Dipti Mishra | Signal Processing | `transform` · `benchmark` | — |
| 2022 | [Learning End-to-End Lossy Image Compression: A Benchmark](https://arxiv.org/abs/2002.03711) | Yueyu Hu | IEEE TPAMI | `transform` · `benchmark` | — |
| 2019 | [Image and Video Compression With Neural Networks: A Review](https://ieeexplore.ieee.org/document/8693636) | Siwei Ma | IEEE TCSVT | `transform` · `benchmark` | — |

## Lossless & Near-lossless Compression

Neural lossless codecs and methods with explicit pointwise reconstruction-error constraints.

| Year | Paper | First author | Venue | Tags | Code / project |
| :--: | --- | --- | --- | --- | :--: |
| 2025 | [Fitted Neural Lossless Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Fitted_Neural_Lossless_Image_Compression_CVPR_2025_paper.html) | Zhe Zhang | CVPR | `lossless` · `overfitted` · `entropy-model` · `adaptation` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/ZZ022/FNLIC.svg?style=social&label=Star)](https://github.com/ZZ022/FNLIC) |
| 2025 | [Large Language Models for Lossless Image Compression: Next-Pixel Prediction in Language Space is All You Need](https://openreview.net/forum?id=FXBBy1caOX) | Kecheng Chen | NeurIPS | `lossless` · `foundation-model` · `entropy-model` | — |
| 2025 | [Towards Lossless Implicit Neural Representation via Bit Plane Decomposition](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Towards_Lossless_Implicit_Neural_Representation_via_Bit_Plane_Decomposition_CVPR_2025_paper.html) | Woo Kyoung Han | CVPR | `lossless` · `inr` · `quantization` | [![Stars](https://img.shields.io/github/stars/WooKyoungHan/LosslessINR.svg?style=social&label=Star)](https://github.com/WooKyoungHan/LosslessINR) |
| 2024 | [Deep Lossy Plus Residual Coding for Lossless and Near-lossless Image Compression](https://ieeexplore.ieee.org/document/10378746) | Yuanchao Bai | IEEE TPAMI | `near-lossless` · `transform` · `entropy-model` · `scalable` | [![Stars](https://img.shields.io/github/stars/BYchao100/Deep-Lossy-Plus-Residual-Coding.svg?style=social&label=Star)](https://github.com/BYchao100/Deep-Lossy-Plus-Residual-Coding) |
| 2024 | [Learned Lossless Image Compression based on Bit Plane Slicing](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learned_Lossless_Image_Compression_based_on_Bit_Plane_Slicing_CVPR_2024_paper.html) | Zhe Zhang | CVPR | `lossless` · `autoregressive` · `entropy-model` | — |
| 2022 | [Learned Lossless Image Compression With Frequency Decomposition Network](https://openaccess.thecvf.com/content/CVPR2022/html/Rhee_LC-FDNet_Learned_Lossless_Image_Compression_With_Frequency_Decomposition_Network_CVPR_2022_paper.html) | Hochang Rhee | CVPR | `lossless` · `autoregressive` · `transform` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/myideaisgood/LC-FDNet.svg?style=social&label=Star)](https://github.com/myideaisgood/LC-FDNet) |
| 2022 | [Practical Image Lossless Compression With an End-to-End GPU Oriented Neural Framework](https://openaccess.thecvf.com/content/CVPR2022/html/Kang_PILC_Practical_Image_Lossless_Compression_With_an_End-to-End_GPU_Oriented_CVPR_2022_paper.html) | Ning Kang | CVPR | `lossless` · `autoregressive` · `entropy-model` · `low-complexity` · `practical` | — |
| 2021 | [IDF++: Analyzing and Improving Integer Discrete Flows for Lossless Compression](https://openreview.net/forum?id=MBOyiNnYthd) | Rianne van den Berg | ICLR | `lossless` · `flow` · `transform` | — |
| 2021 | [iFlow: Numerically Invertible Flows for Efficient Lossless Compression via a Uniform Coder](https://arxiv.org/abs/2111.00965) | Shifeng Zhang | NeurIPS | `lossless` · `flow` · `transform` · `entropy-model` | — |
| 2021 | [Improving Lossless Compression Rates via Monte Carlo Bits-Back Coding](https://arxiv.org/abs/2102.11086) | Yangjun Ruan | ICML | `lossless` · `flow` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/ryoungj/mcbits.svg?style=social&label=Star)](https://github.com/ryoungj/mcbits) |
| 2021 | [iVPF: Numerical Invertible Volume Preserving Flow for Efficient Lossless Compression](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_iVPF_Numerical_Invertible_Volume_Preserving_Flow_for_Efficient_Lossless_Compression_CVPR_2021_paper.html) | Shifeng Zhang | CVPR | `lossless` · `flow` · `transform` | — |
| 2021 | [Learning Scalable l-infinity-constrained Near-lossless Image Compression via Joint Lossy Image and Residual Compression](https://openaccess.thecvf.com/content/CVPR2021/papers/Bai_Learning_Scalable_lY-Constrained_Near-Lossless_Image_Compression_via_Joint_Lossy_Image_CVPR_2021_paper.pdf) | Yuanchao Bai | CVPR | `near-lossless` · `transform` · `entropy-model` · `scalable` | [![Stars](https://img.shields.io/github/stars/BYchao100/Scalable-Near-lossless-Image-Compression.svg?style=social&label=Star)](https://github.com/BYchao100/Scalable-Near-lossless-Image-Compression) |
| 2021 | [OSOA: One-Shot Online Adaptation of Deep Generative Models for Lossless Compression](https://arxiv.org/abs/2111.01662) | Chen Zhang | NeurIPS | `lossless` · `autoregressive` · `adaptation` · `entropy-model` · `content-adaptive` | — |
| 2021 | [Ultra High Fidelity Deep Image Decompression With l-infinity-Constrained Compression](https://ieeexplore.ieee.org/document/9277919) | Xi Zhang | IEEE TIP | `near-lossless` · `transform` · `optimization` | — |
| 2019 | [Practical Full Resolution Learned Lossless Image Compression](https://openaccess.thecvf.com/content_CVPR_2019/html/Mentzer_Practical_Full_Resolution_Learned_Lossless_Image_Compression_CVPR_2019_paper.html) | Fabian Mentzer | CVPR | `lossless` · `autoregressive` · `entropy-model` · `practical` | [![Stars](https://img.shields.io/github/stars/fab-jul/L3C-PyTorch.svg?style=social&label=Star)](https://github.com/fab-jul/L3C-PyTorch) |

## Lossy — Distortion-oriented Coding

Methods primarily optimized for rate-distortion performance using pixel-domain fidelity metrics.

| Year | Paper | First author | Venue | Tags | Code / project |
| :--: | --- | --- | --- | --- | :--: |
| 2026 | [DeepHQ: Learned Hierarchical Quantizer for Progressive Deep Image Coding](https://doi.org/10.1145/3773994) | Jooyoung Lee | ACM TOMM | `distortion` · `transform` · `quantization` · `progressive` · `variable-rate` | — |
| 2025 | [Balanced Rate-Distortion Optimization in Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Balanced_Rate-Distortion_Optimization_in_Learned_Image_Compression_CVPR_2025_paper.html) | Yichi Zhang | CVPR | `distortion` · `transform` · `optimization` | [link](https://gitlab.com/viper-purdue/Balanced-RD) |
| 2025 | [Cassic: Towards Content-Adaptive State-Space Models for Learned Image Compression](https://openaccess.thecvf.com/content/ICCV2025/html/Qin_Cassic_Towards_Content-Adaptive_State-Space_Models_for_Learned_Image_Compression_ICCV_2025_paper.html) | Shiyu Qin | ICCV | `distortion` · `transform` · `entropy-model` · `content-adaptive` · `low-complexity` | — |
| 2025 | [Efficient Progressive Image Compression with Variance-Aware Masking](https://openaccess.thecvf.com/content/WACV2025/html/Presta_Efficient_Progressive_Image_Compression_with_Variance-Aware_Masking_WACV_2025_paper.html) | Elena Presta | WACV | `distortion` · `transform` · `quantization` · `entropy-model` · `progressive` · `variable-rate` · `low-complexity` | — |
| 2025 | [Few-Shot Domain Adaptation for Learned Image Compression](https://doi.org/10.1609/aaai.v39i10.33100) | Tianyu Zhang | AAAI | `distortion` · `transform` · `adaptation` · `content-adaptive` · `low-complexity` | — |
| 2025 | [Knowledge Distillation for Learned Image Compression](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Knowledge_Distillation_for_Learned_Image_Compression_ICCV_2025_paper.html) | Yunuo Chen | ICCV | `distortion` · `transform` · `optimization` · `low-complexity` · `practical` | — |
| 2025 | [Learned Image Compression with Dictionary-based Entropy Model](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Learned_Image_Compression_with_Dictionary-based_Entropy_Model_CVPR_2025_paper.html) | Jingbo Lu | CVPR | `distortion` · `transform` · `entropy-model` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/LabShuHangGU/DCAE.svg?style=social&label=Star)](https://github.com/LabShuHangGU/DCAE) |
| 2025 | [Learned Image Compression with Hierarchical Progressive Context Modeling](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Learned_Image_Compression_with_Hierarchical_Progressive_Context_Modeling_ICCV_2025_paper.html) | Yuqi Li | ICCV | `distortion` · `transform` · `entropy-model` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/lyq133/LIC-HPCM.svg?style=social&label=Star)](https://github.com/lyq133/LIC-HPCM) |
| 2025 | [Linear Attention Modeling for Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_Linear_Attention_Modeling_for_Learned_Image_Compression_CVPR_2025_paper.html) | Donghui Feng | CVPR | `distortion` · `transform` · `entropy-model` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/sjtu-medialab/RwkvCompress.svg?style=social&label=Star)](https://github.com/sjtu-medialab/RwkvCompress) |
| 2025 | [Multirate Neural Image Compression with Adaptive Lattice Vector Quantization](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Multirate_Neural_Image_Compression_with_Adaptive_Lattice_Vector_Quantization_CVPR_2025_paper.html) | Hao Xu | CVPR | `distortion` · `vq` · `quantization` · `adaptation` · `variable-rate` · `content-adaptive` | — |
| 2025 | [Test-time Adaptation for Image Compression with Distribution Regularization](https://openreview.net/forum?id=bsnRUkVn63) | Kecheng Chen | ICLR | `distortion` · `transform` · `adaptation` · `entropy-model` · `content-adaptive` | — |
| 2024 | [BaSIC: BayesNet Structure Learning for Computational Scalable Neural Image Compression](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03640.pdf) | Yufeng Zhang | ECCV | `distortion` · `transform` · `entropy-model` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/worldlife123/cbench_BaSIC.svg?style=social&label=Star)](https://github.com/worldlife123/cbench_BaSIC) |
| 2024 | [Causal Context Adjustment Loss for Learned Image Compression](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f074a994e062146561db9cdc63999efa-Abstract-Conference.html) | Minghao Han | NeurIPS | `distortion` · `transform` · `entropy-model` · `optimization` · `low-complexity` | — |
| 2024 | [WeConvene: Learned Image Compression with Wavelet-Domain Convolution and Entropy Model](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06635.pdf) | Haisheng Fu | ECCV | `distortion` · `transform` · `entropy-model` · `low-complexity` | — |
| 2024 | [Window-based Channel Attention for Wavelet-enhanced Learned Image Compression](https://openaccess.thecvf.com/content/ACCV2024/html/Xu_Window-based_Channel_Attention_for_Wavelet-enhanced_Learned_Image_Compression_ACCV_2024_paper.html) | Heng Xu | ACCV | `distortion` · `transform` | — |
| 2023 | [Learned Image Compression with Mixed Transformer-CNN Architectures](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_Learned_Image_Compression_With_Mixed_Transformer-CNN_Architectures_CVPR_2023_paper.html) | Jinming Liu | CVPR | `distortion` · `transform` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/jmliu206/LIC_TCM.svg?style=social&label=Star)](https://github.com/jmliu206/LIC_TCM) |
| 2023 | [NVTC: Nonlinear Vector Transform Coding](https://openaccess.thecvf.com/content/CVPR2023/html/Feng_NVTC_Nonlinear_Vector_Transform_Coding_CVPR_2023_paper.html) | Runsen Feng | CVPR | `distortion` · `vq` · `transform` · `quantization` | [![Stars](https://img.shields.io/github/stars/USTC-IMCL/NVTC.svg?style=social&label=Star)](https://github.com/USTC-IMCL/NVTC) |
| 2022 | [ELIC: Efficient Learned Image Compression with Unevenly Grouped Space-Channel Contextual Adaptive Coding](https://openaccess.thecvf.com/content/CVPR2022/html/He_ELIC_Efficient_Learned_Image_Compression_With_Unevenly_Grouped_Space-Channel_Contextual_CVPR_2022_paper.html) | Dailan He | CVPR | `distortion` · `transform` · `entropy-model` · `low-complexity` | — |
| 2022 | [The Devil Is in the Details: Window-Based Attention for Image Compression](https://openaccess.thecvf.com/content/CVPR2022/html/Zou_The_Devil_Is_in_the_Details_Window-Based_Attention_for_Image_CVPR_2022_paper.html) | Renjie Zou | CVPR | `distortion` · `transform` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/Googolxx/STF.svg?style=social&label=Star)](https://github.com/Googolxx/STF) |
| 2021 | [Checkerboard Context Model for Efficient Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2021/html/He_Checkerboard_Context_Model_for_Efficient_Learned_Image_Compression_CVPR_2021_paper.html) | Dailan He | CVPR | `distortion` · `transform` · `entropy-model` · `low-complexity` | — |
| 2021 | [Soft Then Hard: Rethinking the Quantization in Neural Image Compression](https://proceedings.mlr.press/v139/guo21c.html) | Zongyu Guo | ICML | `distortion` · `vq` · `quantization` | — |
| 2020 | [Coarse-to-Fine Hyper-Prior Modeling for Learned Image Compression](https://doi.org/10.1609/aaai.v34i07.6696) | Yueyu Hu | AAAI | `distortion` · `transform` · `entropy-model` | — |
| 2020 | [Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules](https://openaccess.thecvf.com/content_CVPR_2020/html/Cheng_Learned_Image_Compression_With_Discretized_Gaussian_Mixture_Likelihoods_and_Attention_CVPR_2020_paper.html) | Zhengxue Cheng | CVPR | `distortion` · `transform` · `entropy-model` | — |
| 2018 | [Joint Autoregressive and Hierarchical Priors for Learned Image Compression](https://proceedings.neurips.cc/paper/2018/hash/53edebc543333dfbf7c5933af792c9c4-Abstract.html) | David Minnen | NeurIPS | `distortion` · `transform` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| 2018 | [Variational Image Compression with a Scale Hyperprior](https://openreview.net/forum?id=rkcQFMZRb) | Johannes Balle | ICLR | `distortion` · `transform` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| 2017 | [End-to-end Optimized Image Compression](https://openreview.net/forum?id=rJxdQ3jeg) | Johannes Balle | ICLR | `distortion` · `transform` · `quantization` · `entropy-model` | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression) |
| 2017 | [Lossy Image Compression with Compressive Autoencoders](https://openreview.net/forum?id=rJiNwv9gg) | Lucas Theis | ICLR | `distortion` · `transform` · `quantization` | — |
| 2017 | [Soft-to-Hard Vector Quantization for End-to-End Learning Compressible Representations](https://proceedings.neurips.cc/paper/2017/hash/86b122d4358357d834a87ce618a55de0-Abstract.html) | Eirikur Agustsson | NeurIPS | `distortion` · `vq` · `quantization` | — |

## Lossy — Perception-oriented Coding

Methods primarily optimized for perceptual quality or the rate-distortion-perception trade-off.

| Year | Paper | First author | Venue | Tags | Code / project |
| :--: | --- | --- | --- | --- | :--: |
| 2026 | [CADC: Content Adaptive Diffusion-Based Generative Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_CADC_Content_Adaptive_Diffusion-Based_Generative_Image_Compression_CVPR_2026_paper.html) | Xihua Sheng | CVPR | `perception` · `diffusion` · `quantization` · `optimization` · `content-adaptive` | — |
| 2026 | [CoD: A Diffusion Foundation Model for Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Jia_CoD_A_Diffusion_Foundation_Model_for_Image_Compression_CVPR_2026_paper.html) | Zhaoyang Jia | CVPR | `perception` · `diffusion` · `foundation-model` · `transform` · `optimization` · `low-complexity` | [![Stars](https://img.shields.io/github/stars/microsoft/GenCodec.svg?style=social&label=Star)](https://github.com/microsoft/GenCodec/tree/main/CoD) |
| 2026 | [DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_DiT-IC_Aligned_Diffusion_Transformer_for_Efficient_Image_Compression_CVPR_2026_paper.html) | Junqi Shi | CVPR | `perception` · `diffusion` · `transform` · `optimization` · `low-complexity` · `practical` | — |
| 2026 | [Ultra-Low Bitrate Perceptual Image Compression with Shallow Encoder](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Ultra-Low_Bitrate_Perceptual_Image_Compression_with_Shallow_Encoder_CVPR_2026_paper.html) | Tianyu Zhang | CVPR | `perception` · `diffusion` · `transform` · `low-complexity` | — |
| 2026 | [What Matters in Practical Learned Image Compression](https://openaccess.thecvf.com/content/CVPR2026/html/Tatwawadi_What_Matters_in_Practical_Learned_Image_Compression_CVPR_2026_paper.html) | Kedar Tatwawadi | CVPR | `perception` · `transform` · `optimization` · `low-complexity` · `practical` · `variable-rate` | — |
| 2025 | [Decouple Distortion from Perception: Region Adaptive Diffusion for Extreme-low Bitrate Perception Image Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Decouple_Distortion_from_Perception_Region_Adaptive_Diffusion_for_Extreme-low_Bitrate_CVPR_2025_paper.html) | Jinchang Xu | CVPR | `perception` · `diffusion` · `optimization` · `content-adaptive` | — |
| 2025 | [Diffusion-based Compression Quality Tradeoffs without Retraining](https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Brenig_Diffusion-based_Compression_Quality_Tradeoffs_without_Retraining_ICCVW_2025_paper.html) | Jonas Brenig | ICCV Workshops | `perception` · `diffusion` · `adaptation` · `optimization` · `content-adaptive` | — |
| 2025 | [Good, Cheap, and Fast: Overfitted Image Compression with Wasserstein Distortion](https://openaccess.thecvf.com/content/CVPR2025/html/Balle_Good_Cheap_and_Fast_Overfitted_Image_Compression_with_Wasserstein_Distortion_CVPR_2025_paper.html) | Jona Balle | CVPR | `perception` · `overfitted` · `optimization` · `low-complexity` | — |
| 2023 | [Lossy Image Compression with Conditional Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ccf6d8b4a1fe9d9c8192f00c713872ea-Abstract-Conference.html) | Ruihan Yang | NeurIPS | `perception` · `diffusion` · `transform` · `optimization` | [![Stars](https://img.shields.io/github/stars/buggyyang/CDC_compression.svg?style=social&label=Star)](https://github.com/buggyyang/CDC_compression) |
| 2020 | [High-Fidelity Generative Image Compression](https://proceedings.neurips.cc/paper/2020/hash/8a50bae297807da9e97722a0b3fd8f27-Abstract.html) | Fabian Mentzer | NeurIPS | `perception` · `gan` · `optimization` | [![Stars](https://img.shields.io/github/stars/tensorflow/compression.svg?style=social&label=Star)](https://github.com/tensorflow/compression/tree/master/models/hific) |
| 2019 | [Generative Adversarial Networks for Extreme Learned Image Compression](https://openaccess.thecvf.com/content_ICCV_2019/html/Agustsson_Generative_Adversarial_Networks_for_Extreme_Learned_Image_Compression_ICCV_2019_paper.html) | Eirikur Agustsson | ICCV | `perception` · `gan` · `quantization` · `optimization` | — |
| 2019 | [Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff](https://proceedings.mlr.press/v97/blau19a.html) | Yochai Blau | ICML | `perception` · `gan` · `optimization` | — |
