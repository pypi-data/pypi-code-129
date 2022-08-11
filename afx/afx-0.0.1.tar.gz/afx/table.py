from dynamojo import Lsi, Gsi, TableIndex, IndexList


desc = {
  "gsi": [
    {
      "IndexName": "gsi15",
      "KeySchema": [
        {
          "AttributeName": "gsi15_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi15_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi14",
      "KeySchema": [
        {
          "AttributeName": "gsi14_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi14_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi17",
      "KeySchema": [
        {
          "AttributeName": "gsi17_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi17_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi16",
      "KeySchema": [
        {
          "AttributeName": "gsi16_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi16_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi19",
      "KeySchema": [
        {
          "AttributeName": "gsi19_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi19_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi18",
      "KeySchema": [
        {
          "AttributeName": "gsi18_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi18_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi0",
      "KeySchema": [
        {
          "AttributeName": "gsi0_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi0_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi1",
      "KeySchema": [
        {
          "AttributeName": "gsi1_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi1_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi2",
      "KeySchema": [
        {
          "AttributeName": "gsi2_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi2_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi3",
      "KeySchema": [
        {
          "AttributeName": "gsi3_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi3_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi4",
      "KeySchema": [
        {
          "AttributeName": "gsi4_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi4_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi5",
      "KeySchema": [
        {
          "AttributeName": "gsi5_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi5_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi6",
      "KeySchema": [
        {
          "AttributeName": "gsi6_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi6_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi7",
      "KeySchema": [
        {
          "AttributeName": "gsi7_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi7_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi8",
      "KeySchema": [
        {
          "AttributeName": "gsi8_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi8_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi9",
      "KeySchema": [
        {
          "AttributeName": "gsi9_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi9_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi11",
      "KeySchema": [
        {
          "AttributeName": "gsi11_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi11_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi10",
      "KeySchema": [
        {
          "AttributeName": "gsi10_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi10_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi13",
      "KeySchema": [
        {
          "AttributeName": "gsi13_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi13_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "gsi12",
      "KeySchema": [
        {
          "AttributeName": "gsi12_pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "gsi12_sk",
          "KeyType": "RANGE"
        }
      ]
    }
  ],
  "lsi": [
    {
      "IndexName": "lsi4",
      "KeySchema": [
        {
          "AttributeName": "pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "lsi4_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "lsi2",
      "KeySchema": [
        {
          "AttributeName": "pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "lsi2_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "lsi3",
      "KeySchema": [
        {
          "AttributeName": "pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "lsi3_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "lsi0",
      "KeySchema": [
        {
          "AttributeName": "pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "lsi0_sk",
          "KeyType": "RANGE"
        }
      ]
    },
    {
      "IndexName": "lsi1",
      "KeySchema": [
        {
          "AttributeName": "pk",
          "KeyType": "HASH"
        },
        {
          "AttributeName": "lsi1_sk",
          "KeyType": "RANGE"
        }
      ]
    }
  ],
  "table_index": {
    "IndexName": "table",
    "KeySchema": [
      {
        "AttributeName": "pk",
        "KeyType": "HASH"
      },
      {
        "AttributeName": "sk",
        "KeyType": "RANGE"
      }
    ]
  }
}

def get_indexes() -> IndexList:

    gsi_list = desc["gsi"]
    lsi_list = desc["lsi"]

    table_list = [{"IndexName": "table", "KeySchema": desc["table_index"]["KeySchema"]}]

    def build_indexes(index_type, index_list):
        index_objects = []
        for index in index_list:
            args = {}
            args["name"] = index["IndexName"]

            for attr in index["KeySchema"]:
                if attr["KeyType"] == "HASH" and index_type != Lsi:
                    args["partitionkey"] = attr["AttributeName"]
                elif attr["KeyType"] == "RANGE":
                    args["sortkey"] = attr["AttributeName"]

            index_objects.append(index_type(**args))

        return index_objects

    indexes = IndexList(
        *[
            *build_indexes(Gsi, gsi_list),
            *build_indexes(Lsi, lsi_list),
            *build_indexes(TableIndex, table_list),
        ]
    )
    return indexes
