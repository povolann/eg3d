# SPDX-FileCopyrightText: Copyright (c) 2021-2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import os
import shutil
import tempfile
import subprocess


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as working_dir:
        output_dataset_name = 'chest_128.zip'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_path = '/home/anya/Programs/eg3d/dataset_preprocessing/chest/chest/'

        print("Converting camera parameters...")
        cmd = f"python {os.path.join(dir_path, 'preprocess_chest_cameras.py')} --source={data_path}"
        subprocess.run([cmd], shell=True)

        print("Creating dataset zip...")
        cmd = f"python {os.path.join(dir_path, '../../eg3d', 'dataset_tool.py')}"
        cmd += f" --source {data_path} --dest {output_dataset_name} --resolution 128x128"
        subprocess.run([cmd], shell=True)