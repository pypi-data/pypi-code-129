# Copyright (c) Kuba Szczodrzyński 2022-07-29.

import sys
from os.path import dirname, join

sys.path.append(join(dirname(__file__), "..", "..", ".."))

from argparse import ArgumentParser, FileType
from io import SEEK_SET, FileIO
from os import stat
from time import time
from typing import Union

from util import RBL, BekenBinary, OTACompression, OTAEncryption

from ltchiptool.util.intbin import ByteGenerator, fileiter


def auto_int(x):
    return int(x, 0)


def add_common_args(parser):
    parser.add_argument(
        "coeffs", type=str, help="Encryption coefficients (hex string, 32 chars)"
    )
    parser.add_argument("input", type=FileType("rb"), help="Input file")
    parser.add_argument("output", type=FileType("wb"), help="Output file")
    parser.add_argument("addr", type=auto_int, help="Memory address (dec/hex)")


def add_package_args(parser):
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Firmware name (default: app)",
        default="app",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--version",
        type=str,
        help="Firmware version (default: 1.00)",
        default="1.00",
        required=False,
    )


if __name__ == "__main__":
    parser = ArgumentParser(description="Encrypt/decrypt Beken firmware binaries")
    sub = parser.add_subparsers(dest="action", required=True)

    encrypt = sub.add_parser("encrypt", help="Encrypt binary files without packaging")
    add_common_args(encrypt)
    encrypt.add_argument("-c", "--crc", help="Include CRC16", action="store_true")

    decrypt = sub.add_parser("decrypt", description="Decrypt unpackaged binary files")
    add_common_args(decrypt)
    decrypt.add_argument(
        "-C",
        "--no-crc-check",
        help="Do not check CRC16 (if present)",
        action="store_true",
    )

    package = sub.add_parser(
        "package", description="Package raw binary files as RBL containers"
    )
    add_common_args(package)
    package.add_argument(
        "size", type=auto_int, help="RBL total size (excl. CRC) (dec/hex)"
    )
    add_package_args(package)

    unpackage = sub.add_parser(
        "unpackage", description="Unpackage a single RBL container"
    )
    add_common_args(unpackage)
    unpackage.add_argument(
        "offset", type=auto_int, help="Offset in input file (dec/hex)"
    )
    unpackage.add_argument(
        "size", type=auto_int, help="Container total size (incl. CRC) (dec/hex)"
    )

    ota = sub.add_parser("ota", description="Package OTA firmware")
    ota.add_argument("input", type=FileType("rb"), help="Input file")
    ota.add_argument("output", type=FileType("wb"), help="Output file")
    ota.add_argument(
        "compress", type=str, help="Compression algorithm (none/quicklz/fastlz/gzip)"
    )
    ota.add_argument("encrypt", type=str, help="Encryption algorithm (none/aes256)")
    ota.add_argument("--key", type=str, required=False, help="AES256 key (optional)")
    ota.add_argument("--iv", type=str, required=False, help="AES256 IV (optional)")
    add_package_args(ota)

    deota = sub.add_parser("deota", description="Un-package OTA firmware")
    deota.add_argument("input", type=FileType("rb"), help="Input file")
    deota.add_argument("output", type=FileType("wb"), help="Output file")
    deota.add_argument("--key", type=str, required=False, help="AES256 key (optional)")
    deota.add_argument("--iv", type=str, required=False, help="AES256 IV (optional)")
    add_package_args(deota)

    args = parser.parse_args()
    bk = BekenBinary(args.coeffs if "ota" not in args.action else None)
    f: FileIO = args.input
    size = stat(args.input.name).st_size
    start = time()
    gen: Union[ByteGenerator, None] = None

    if args.action == "encrypt":
        print(f"Encrypting '{f.name}' ({size} bytes)")
        if args.crc:
            print(f" - calculating 32-byte block CRC16...")
            gen = bk.crc(bk.crypt(args.addr, f))
        else:
            print(f" - as raw binary, without CRC16...")
            gen = bk.crypt(args.addr, f)

    if args.action == "decrypt":
        print(f"Decrypting '{f.name}' ({size} bytes)")
        if size % 34 == 0:
            if args.no_crc_check:
                print(f" - has CRC16, skipping checks...")
            else:
                print(f" - has CRC16, checking...")
            gen = bk.crypt(args.addr, bk.uncrc(f, check=not args.no_crc_check))
        elif size % 4 != 0:
            raise ValueError("Input file has invalid length")
        else:
            print(f" - raw binary, no CRC")
            gen = bk.crypt(args.addr, f)

    if args.action == "package":
        print(f"Packaging {args.name} '{f.name}' for memory address 0x{args.addr:X}")
        rbl = RBL(name=args.name, version=args.version)
        if args.name == "bootloader":
            rbl.has_part_table = True
            print(f" - in bootloader mode; partition table unencrypted")
        rbl.container_size = args.size
        print(f" - container size (excl. CRC): 0x{rbl.container_size:X}")
        print(f" - container size (incl. CRC): 0x{rbl.container_size_crc:X}")
        gen = bk.package(f, args.addr, size, rbl)

    if args.action == "unpackage":
        print(f"Unpackaging '{f.name}' (at 0x{args.offset:X}, size 0x{args.size:X})")
        f.seek(args.offset + args.size - 102, SEEK_SET)
        rbl = f.read(102)
        rbl = b"".join(bk.uncrc(rbl))
        rbl = RBL.deserialize(rbl)
        print(f" - found '{rbl.name}' ({rbl.version}), size {rbl.data_size}")
        f.seek(0, SEEK_SET)
        crc_size = (rbl.data_size - 16) // 32 * 34
        gen = bk.crypt(args.addr, bk.uncrc(fileiter(f, 32, 0xFF, crc_size)))

    algo_comp = {
        "none": OTACompression.NONE,
        "quicklz": OTACompression.QUICKLZ,
        "fastlz": OTACompression.FASTLZ,
        "gzip": OTACompression.GZIP,
    }
    algo_encr = {
        "none": OTAEncryption.NONE,
        "aes256": OTAEncryption.AES256,
    }
    if args.action == "ota":
        if args.compress not in algo_comp:
            raise ValueError("Invalid compression algorithm")
        if args.encrypt not in algo_encr:
            raise ValueError("Invalid encryption algorithm")
        print(
            f"OTA packaging '{f.name}' with compression '{args.compress}' and encryption '{args.encrypt}'"
        )
        rbl = RBL(
            name=args.name,
            version=args.version,
            compression=algo_comp[args.compress],
            encryption=algo_encr[args.encrypt],
        )
        gen = bk.ota_package(f, rbl, key=args.key, iv=args.iv)

    if args.action == "deota":
        print(f"OTA un-packaging '{f.name}'")
        rbl = f.read(96)
        rbl = RBL.deserialize(rbl)
        print(
            f" - found '{rbl.name}' ({rbl.version}),",
            f"size {rbl.raw_size},",
            f"compression {rbl.compression.name},",
            f"encryption {rbl.encryption.name}",
        )
        gen = bk.ota_unpackage(f, rbl, key=args.key, iv=args.iv)

    if not gen:
        raise RuntimeError("gen is None")

    written = 0
    for data in gen:
        args.output.write(data)
        written += len(data)
    print(f" - wrote {written} bytes in {time()-start:.3f} s")
