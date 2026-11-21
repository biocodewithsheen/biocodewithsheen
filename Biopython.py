{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPXMFzfCzaly2BWC57UOOXt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/biocodewithsheen/biocodewithsheen/blob/main/Biopython.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install Bio\n",
        "import Bio\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "evVFrafj1quq",
        "outputId": "bc0fbae2-aa1d-4886-f03f-4e7c7e464a8d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: Bio in /usr/local/lib/python3.13/dist-packages (1.8.5)\n",
            "Requirement already satisfied: biopython>=1.80 in /usr/local/lib/python3.13/dist-packages (from Bio) (1.88)\n",
            "Requirement already satisfied: gprofiler-official in /usr/local/lib/python3.13/dist-packages (from Bio) (1.0.0)\n",
            "Requirement already satisfied: mygene in /usr/local/lib/python3.13/dist-packages (from Bio) (3.2.2)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.13/dist-packages (from Bio) (2.2.3)\n",
            "Requirement already satisfied: pooch in /usr/local/lib/python3.13/dist-packages (from Bio) (1.9.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.13/dist-packages (from Bio) (2.32.4)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.13/dist-packages (from Bio) (4.67.3)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.13/dist-packages (from biopython>=1.80->Bio) (2.4.6)\n",
            "Requirement already satisfied: biothings-client>=0.2.6 in /usr/local/lib/python3.13/dist-packages (from mygene->Bio) (0.5.1)\n",
            "Requirement already satisfied: httpx<1.0,>=0.25.0 in /usr/local/lib/python3.13/dist-packages (from biothings-client>=0.2.6->mygene->Bio) (0.28.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.13/dist-packages (from httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (4.16.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.13/dist-packages (from httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (2026.10.23)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.13/dist-packages (from httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (1.0.9)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.13/dist-packages (from httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (3.20)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.13/dist-packages (from httpcore==1.*->httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (0.16.0)\n",
            "Requirement already satisfied: typing_extensions>=4.16.0 in /usr/local/lib/python3.13/dist-packages (from anyio->httpx<1.0,>=0.25.0->biothings-client>=0.2.6->mygene->Bio) (4.16.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.13/dist-packages (from pandas->Bio) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.13/dist-packages (from pandas->Bio) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.13/dist-packages (from pandas->Bio) (2026.6)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.13/dist-packages (from python-dateutil>=2.8.2->pandas->Bio) (1.17.0)\n",
            "Requirement already satisfied: platformdirs>=2.5.0 in /usr/local/lib/python3.13/dist-packages (from pooch->Bio) (4.14.3)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.13/dist-packages (from pooch->Bio) (26.3)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.13/dist-packages (from requests->Bio) (3.4.9)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.13/dist-packages (from requests->Bio) (2.5.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from Bio.Seq import Seq"
      ],
      "metadata": {
        "id": "D4r6CIME3T-w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dna=(\"ATGGCTAT\")\n",
        "print(dna)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vR-8agfE3Z6h",
        "outputId": "f59511c4-5c5d-41a1-c9ef-38eb40609bb4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ATGGCTAT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "zDcyz5S74nyW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dna_=Seq(dna)\n",
        "print(dna_.complement())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xYzsKwPO4pQU",
        "outputId": "6df2eee7-8481-4a9c-e755-8284a8cbcde6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TACCGATA\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"dna:\",dna_)\n",
        "print(\"rna:\",dna_.transcribe())\n",
        "print(\"protein:\",dna_.translate())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hAgDc1re6eJz",
        "outputId": "c2e17dbd-74b4-4818-d637-b786261ab273"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dna: ATGGCTAT\n",
            "rna: AUGGCUAU\n",
            "protein: MA\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from Bio.SeqRecord import SeqRecord\n",
        "\n"
      ],
      "metadata": {
        "id": "i0Fp6j5k8ciI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}