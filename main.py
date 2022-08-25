# imports
# import yaml
# from read_excel import ReadExcel
#
#
# class Driver:
#     # variables
#     host: ""
#     token: ""
#     project: ""
#     collection: ""
#     excel_absolute_path: ""
#     public: False
#
#     def __int__(self, config_file_absolute_path: str):
#         """
#         takes config file as absolute path, gets the variables from it,
#         then sets them in python, so they can be used easily
#
#         alternatively, this can be done with just python variables and remove the yml file
#
#         :param config_file_absolute_path: str
#         :return:
#         """
#
#         # read the config file
#         with open(config_file_absolute_path, "r") as file:
#             config_file = yaml.safe_load(file)
#
#             # setting up variables to be used by rest of the program
#             # TODO error handling in case the file or field is missing can be done here
#             self.host = config_file["host"]
#             self.token = config_file["token"]
#             self.project = config_file["project"]
#             self.collection = config_file["collection"]
#             self.excel_absolute_path = config_file["excel_absolute_path"]
#             self.public = config_file["public"]
#
#
# def set_cript_requirements(config_file_absolute_path: str):
#     """
#     get config variables and set our variables to be used through the rest of the script
#     :param config_file_absolute_path: str
#     :return:
#     """
#     with open(config_file_absolute_path, "r") as file:
#         config_file = yaml.safe_load(file)


from read_excel import ReadExcel

if __name__ == "__main__":
    read_excel = ReadExcel()
    materials_df = read_excel.get_materials_and_product_sheet()

    # my_upload = Upload()
    #
    # # todo this needs a try except in case the materials returned are None
    # my_upload.upload_materials(materials_df)
