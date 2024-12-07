import torch  # noqa: F401
import torch.nn as nn
import librosa
import torch
import numpy as np
from speechbrain.nnet.CNN import Conv1d
from speechbrain.nnet.linear import Linear
from speechbrain.nnet.normalization import BatchNorm1d
from speechbrain.nnet.pooling import StatisticsPooling

class Xvector(torch.nn.Module):
    def __init__(
        self,
        device="cpu",
        activation=torch.nn.LeakyReLU,
        tdnn_blocks=5,
        tdnn_channels=[512, 512, 512, 512, 1500],
        tdnn_kernel_sizes=[5, 3, 3, 1, 1],
        tdnn_dilations=[1, 2, 3, 1, 1],
        lin_neurons=512,
        in_channels=40,
    ):
        super().__init__()
        self.blocks = nn.ModuleList()

        # TDNN layers
        for block_index in range(tdnn_blocks):
            out_channels = tdnn_channels[block_index]
            self.blocks.extend(
                [
                    Conv1d(
                        in_channels=in_channels,
                        out_channels=out_channels,
                        kernel_size=tdnn_kernel_sizes[block_index],
                        dilation=tdnn_dilations[block_index],
                    ),
                    activation(),
                    BatchNorm1d(input_size=out_channels),
                ]
            )
            in_channels = tdnn_channels[block_index]

        # Statistical pooling
        self.blocks.append(StatisticsPooling())

        # Final linear transformation
        self.blocks.append(
            Linear(
                input_size=out_channels * 2,
                n_neurons=lin_neurons,
                bias=True,
                combine_dims=False,
            )
        )

    def forward(self, x, lens=None):
        for layer in self.blocks:
            try:
                x = layer(x, lengths=lens)
            except TypeError:
                x = layer(x)
        return x


def extract_mfcc(audio_path, sr=16000, n_mfcc=40):
    """بارگذاری فایل صوتی و استخراج MFCC"""
    signal, sr = librosa.load(audio_path, sr=sr) # بارگذاری فایل
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc) # استخراج MFCC
    mfcc_tensor = torch.tensor(mfcc_features.T).unsqueeze(0) # تبدیل به Tensor
    return mfcc_tensor


def extract_xvector(audio_path):
    """استخراج X-vector از فایل صوتی"""
    # استخراج ویژگی‌های MFCC
    mfcc_tensor = extract_mfcc(audio_path)

    # بارگذاری مدل
    model = Xvector(device="cpu") # استفاده از CPU (برای GPU از "cuda" استفاده کنید)
    model.eval()

    # عبور ویژگی‌ها از مدل
    with torch.no_grad():
        xvector = model(mfcc_tensor)
    return xvector

def save_xvector(xvector, output_path="xvector.npy"):
    """ذخیره X-vector به عنوان فایل NumPy"""
    xvector_np = xvector.numpy()
    np.save(output_path, xvector_np)
    print(f"X-vector ذخیره شد در: {output_path}")


if __name__ == "__main__":
    audio_path = r"E:\University\master\mbaheseVijeh\Voice_Conversion\librispeech_dev_clean\LibriSpeech\dev-clean\1272\135031\1272-135031-0000.flac" # مسیر فایل صوتی 
    xvector = extract_xvector(audio_path) # استخراج X-vector
    print("شکل خروجی X-vector:", xvector.shape)
    save_xvector(xvector, "xvector.npy") # ذخیره بردار خروجی

