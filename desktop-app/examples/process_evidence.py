from __future__ import print_function
import argparse
import os
import pytsk3
import pyewf
import sys
from tabulate import tabulate

class EWFImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self._ewf_handle = ewf_handle
        super(EWFImgInfo, self).__init__(url="",
                                         type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self._ewf_handle.close()

    def read(self, offset, size):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()


def main(image, img_type, part_type):
    print("[+] Opening {}".format(image))
    if img_type == "ewf":
        try:
            filenames = pyewf.glob(image)
        except IOError:
            print("[-] Invalid EWF format:\n {}".format(e))
            sys.exit(2)

        ewf_handle = pyewf.handle()
        ewf_handle.open(filenames)
        e01_metadata(ewf_handle)

        # Open PYTSK3 handle on EWF Image
        img_info = EWFImgInfo(ewf_handle)
    else:
        img_info = pytsk3.Img_Info(image)
    #print(img_info)
    try:
        if part_type is not None:
            attr_id = getattr(pytsk3, "TSK_VS_TYPE_" + part_type)
            volume = pytsk3.Volume_Info(img_info, attr_id)
        else:
            volume = pytsk3.Volume_Info(img_info)
    except IOError:
        _, e, _ = sys.exc_info()
        print("[-] Unable to read partition table:\n {}".format(e))
        sys.exit(3)
    part_metadata(volume)


def part_metadata(vol):
    table = [["Index", "Type", "Offset Start (Sectors)",
              "Length (Sectors)"]]
    for part in vol:
        table.append([part.addr, part.desc.decode("utf-8"), part.start,
                      part.len])
    print("\n Partition Metadata")
    print("-" * 20)
    print(tabulate(table, headers="firstrow"))


def e01_metadata(e01_image):
    print("\nEWF Acquisition Metadata")
    print("-" * 20)
    headers = e01_image.get_header_values()
    hashes = e01_image.get_hash_values()
    for k in headers:
        print("{}: {}".format(k, headers[k]))
    for h in hashes:
        print("Acquisition {}: {}".format(h, hashes[h]))
    print("Bytes per Sector: {}".format(e01_image.bytes_per_sector))
    print("Number of Sectors: {}".format(
        e01_image.get_number_of_sectors()))
    print("Total Size: {}".format(e01_image.get_media_size()))

__authors__ = ["OluwaTosin Ayanda"]
__date__ = 20230310
__description__ = "Process Evidence"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__description__,
        epilog="Developed by {} on {}".format(
            ", ".join(__authors__), __date__)
    )
    parser.add_argument("EVIDENCE_FILE", help="Evidence file path")
    parser.add_argument("TYPE", help="Type of Evidence",
                        choices=("raw", "ewf"))
    parser.add_argument("-p", help="Partition Type",
                        choices=("DOS", "GPT", "MAC", "SUN"))
    args = parser.parse_args()

    if os.path.exists(args.EVIDENCE_FILE) and \
            os.path.isfile(args.EVIDENCE_FILE):
        main(args.EVIDENCE_FILE, args.TYPE, args.p)
    else:
        print("[-] Supplied input file {} does not exist or is not a "
              "file".format(args.EVIDENCE_FILE))
        sys.exit(1)
