HTA201_1_1/
│
├── *.ndpi                                       [116 .ndpi]  Raw whole-slide images (Hamamatsu scanner format) — source files for all downstream processing
│
├── 10x/                                          [93 .tif]  High-magnification (1micron/pixel) raw tissue tile images
│   ├── classification_01_30_2025_LGHG_02_27_2026/          Tissue classification outputs (two runs)
│   │   ├── check_classification/                [93 .jpg]  QC overlays to visually verify classifications
│   │   ├── classification_01_30_2025_LGHG/      [92 .tif]  Classification maps — run Jan 2025 (LG/HG labels)
│   │   └── classification_02_27_2026/           [92 .tif]  Classification maps — updated run Feb 2026
│   └── skip/                                    [25 .tif]  Tiles excluded from analysis (low quality / artifacts)
│
├── 1x/                                            [93 .tif]  Low-magnification (8micron/pixel) overview tissue images
│   ├── TA/                                       [116 .tif]  Tissue area (TA) masks or annotations at 1x
│   ├── registered_2025/                           [92 .jpg]  Images registered to a common atlas/reference (2025)
│   │   └── elastic registration/                 [92 .jpg]  Root-level elastically warped registered images
│   │       ├── check/                            [92 .jpg]  QC overlays to verify elastic registration quality
│   │       ├── regisration_metrics/          [1 .fig, 1 .jpg, 1 .mat]  Summary metrics & figures evaluating registration accuracy
│   │       └── save_warps/                       [92 .mat]  Saved warp/displacement fields (MATLAB format)
│   │           └── D/                            [92 .mat]  Deformation field components (D-matrices) per slide
│   └── skip/                                      [24 .tif]  Tiles excluded from analysis(low quality / artifacts)
│
│
├── StarDist_wcc_02_24_2026_96_nrays/                        Nuclear segmentation results (StarDist model, Feb 2026, 96 rays)
│   ├── feature_mat/                              [78 .mat]  Per-nucleus feature matrices (MATLAB format)
│   ├── feature_pickles/                          [78 .pkl]  Per-nucleus feature matrices (Python pickle format)
│   ├── geojsons/                              [78 .geojson]  Nuclear polygon boundaries (GeoJSON for QuPath/viewer)
│   ├── segmentation_masks/                       [78 .tif]  Binary/label masks of segmented nuclei
│   └── segmentation_analysis/                               Analysis of segmentation results
│       └── pix_res_info/                        [116 .mat]  Pixel resolution metadata per slide
│
└── registered_ome/                              [92 .ome.tif]  Multi-channel OME-TIFF images registered across slides
    └── validation_overlay/                        [92 .jpg]  Overlay JPEGs to validate registration quality
