










krogoth_libs = ["moho_extractor", "rest_auth", "kbot_lab"]


for dir in os.listdir("."):
    dir_match = dir[0:8]
    if dir_match == "krogoth_":
        krogoth_libs.append(dir)


print("ALL INSTALLED KROGOTH LIBS: ")
for lib in krogoth_libs:
    print(lib, end=", ")

print("")

