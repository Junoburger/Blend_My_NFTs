# Some code in this file was generously sponsored by the amazing team over at SolSweepers!
# Feel free to check out their amazing project and see how they are using Blend_My_NFTs:
# https://discord.gg/QTT7dzcuVs

# Purpose:
# This file returns the specified meta data format to the Exporter.py for a given NFT DNA.

import bpy
import os
import sys
import importlib


def returnCardanoMetaData(name, NFT_DNA, NFT_Variants):
    metaDataDictCardano = {"721": {
        "<policy_id>": {
            name: {
                "name": name,
                "image": "",
                "mediaType": "",
                "description": "",

            }
        },
        "version": "1.0"
    }}

    for i in NFT_Variants:
        metaDataDictCardano["721"]["<policy_id>"][name][i] = NFT_Variants[i]

    return metaDataDictCardano

def returnSolanaMetaData(name, NFT_DNA, NFT_Variants):
    metaDataDictSolana = {"name": name, "symbol": "", "description": "", "seller_fee_basis_points": None,
                          "image": "", "animation_url": "", "external_url": ""}

    attributes = []

    for i in NFT_Variants:
        dictionary = {
            "trait_type": i,
            "value": NFT_Variants[i]
        }

        attributes.append(dictionary)

    metaDataDictSolana["attributes"] = attributes
    metaDataDictSolana["collection"] = {
        "name": "",
        "family": ""
    }

    metaDataDictSolana["properties"] = {
        "files": [{"uri": "", "type": ""}],
        "category": "",
        "creators": [{"address": "", "share": None}]
    }
    return metaDataDictSolana

def returnErc721MetaData(name, NFT_DNA, NFT_Variants):
    metaDataDictErc721 = {
        "name": name,
        "description": "",
        "image": "",
        "attributes": None,
    }

    attributes = []

    for i in NFT_Variants:
        dictionary = {
            "trait_type": i,
            "value": NFT_Variants[i]
        }

        attributes.append(dictionary)

    metaDataDictErc721["attributes"] = attributes

    return metaDataDictErc721


if __name__ == '__main__':
    returnSolanaMetaData()
    returnCardanoMetaData()
    returnErc721MetaData()
