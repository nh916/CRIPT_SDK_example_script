import math

import cript
from pandas import Series

import cript_variables
import pandas as pd


class ReadExcel:
    excel_file_path = "./assets/Mixture_template.xlsx"
    upload_to_cript = None

    access_group = None
    project = None
    project_collection = None
    public = False

    api = None

    def __init__(self):
        # set up cript api
        self.api = cript.API(host=cript_variables.host, token=cript_variables.token)

        # set up cript nodes that'll be used for everything else
        self.access_group = self.api.get(cript.Group, {"name": cript_variables.access_group_name})
        self.project = self.api.get(cript.Project, {"name": cript_variables.project_name})
        self.project_collection = self.api.get(cript.Collection, {"name": cript_variables.collection_name})

    #     read Excel file and returns a dict
    def get_materials_and_product_sheet(self, excel_file_path=excel_file_path):
        df = pd.read_excel(excel_file_path, sheet_name="Materials and Products")

        for row in df.iterrows():
            # iterate over rows
            # turn each row into a dict
            # put things in correct places

            # row = dict(row.loc["materials"])

            row = row[1]

            # print(type(row))
            # print(not pd.isnull(row["materials"]))
            # print("-------------------------------------------------")

            # check if there is a row, so we don't get errors
            if not pd.isnull(row["materials"]):

                # instantiate material object
                material = cript.Material(project=self.project, name=row["materials"])

                # instantiate property then add it to material
                if not pd.isnull(row["density(g/ml)"]):
                    print(row["density(g/ml)"])
                    property_density = cript.Property(key="density", unit="g/ml", value=row["density(g/ml)"])
                    material.add_property(property_density)

                if not pd.isnull(row["color"]):
                    property_color = cript.Property(key="color", value=row["color"])
                    material.add_property(property_color)

                if not pd.isnull(row["optical transparency at 40 C"]):
                    property_transparency = cript.Property(key="optical_transparency",
                                                           value=row["optical transparency at 40 C"])
                    material.add_property(property_transparency)

                if not pd.isnull(row["elastic modulus(MPa)"]):
                    property_elasticity = cript.Property(key="modulus_elastic", unit="MPa",
                                                         value=row["elastic modulus(MPa)"])
                    material.add_property(property_elasticity)

                if not pd.isnull(row["+/- for elastic modulus "]):
                    # todo is this key right? I have the same key above, is this one a custom key?
                    property_elastic_modulus = cript.Property(key="modulus_elastic", unit="MPa",
                                                              value=row["+/- for elastic modulus "])
                    material.add_property(property_elastic_modulus)

                # self.api.save(material)

            # the process product becomes is also a material
            if not pd.isnull(row["Product"]):
                # instantiate a material
                process_product = cript.Material(project=self.project, name=row["Product"])

                # instantiate property and add it to material
                if not pd.isnull(row["molecular weight average (g/mol)"]):
                    property_molecular_weight = cript.Property(key="mw_w", unit="g/mol",
                                                               value=row["molecular weight average (g/mol)"])
                    process_product.add_property(property_molecular_weight)

                if not pd.isnull(row["color.1"]):
                    # todo is this key correct? there are several keys that could go here
                    property_color = cript.Property(key="color",
                                                    value=row["color.1"])
                    process_product.add_property(property_color)

                if not pd.isnull(row["toughness(J/m**3)"]):
                    property_melting_temperature = cript.Property(key="toughness", unit="J / m**3",
                                                                  value=row["toughness(J/m**3)"])
                    process_product.add_property(property_melting_temperature)

                # self.api.save(process_product)
