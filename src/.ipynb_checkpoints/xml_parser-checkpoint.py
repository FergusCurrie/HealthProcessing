import xml.etree.ElementTree as ET
import pandas as pd


def parse_export_cda(fn: str) -> pd.DataFrame:
    """
    Looks like interested in the entry
    """
    with open(fn) as xmlfile:
        tree = ET.parse(xmlfile)
    root = tree.getroot()
    data = []
    for observation in root.findall(".//{*}observation"):

        value, unit = None, None
        for v in observation.findall(".//{*}value"):
            if "value" in v.attrib and "unit" in v.attrib:
                value = v.attrib["value"]
                unit = v.attrib["unit"]
        display_name = observation.find("./{*}code").attrib["displayName"]
        effective_time_element = observation.find("./{*}effectiveTime")
        effective_time_low = effective_time_element[0].attrib["value"]
        effective_time_high = effective_time_element[1].attrib["value"]
        data.append(
            [value, unit, display_name, effective_time_low, effective_time_high]
        )

    return pd.DataFrame(
        data=data,
        columns=[
            "value",
            "unit",
            "display_name",
            "effective_time_low",
            "effective_time_high",
        ],
    )


def parse_export(fn: str) -> pd.DataFrame:
    with open(fn) as xmlfile:
        tree = ET.parse(xmlfile)
    root = tree.getroot()
    data = []
    for record in root.findall(".//{*}Record"):
        if not "value" in record.attrib:
            continue
        data.append(
            [
                record.attrib["type"],
                record.attrib["creationDate"],
                record.attrib["startDate"],
                record.attrib["endDate"],
                record.attrib["value"],
            ]
        )
        if len(record.attrib["value"]) > 10:
            print(record.attrib["value"])
    return pd.DataFrame(
        data=data, columns=["type", "creationDate", "startDate", "endDate", "value"]
    )


# df = parse_export_cda("../data/apple_health_export/export_cda.xml")
# print(df.head())
# print(df["display_name"].value_counts())

# df = parse_export("../data/apple_health_export/export.xml")
# print(df.head())
# print(df["type"].value_counts())
