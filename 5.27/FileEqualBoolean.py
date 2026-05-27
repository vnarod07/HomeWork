import os, filecmp


def DirectoryEquals(dir1, dir2):
    with os.scandir(dir1) as it:
        l1 = sorted(it, key=lambda e : e.name)
    with os.scandir(dir2) as takestwo:
        l2 = sorted(takestwo, key=lambda e : e.name)
    if len(l1) != len(l2): return False
    for i in range(len(l1)):
        if l1[i].name != l2[i].name: return False
        if l1[i].is_file() != l2[i].is_file(): return False
        if l1[i].is_file():
            if l1[i].stat().st_size != l2[i].stat().st_size: return False
            if not filecmp.cmp(l1[i].path, l2[i].path, shallow=False): return False
    return True

DirectoryEquals(input(), input())
