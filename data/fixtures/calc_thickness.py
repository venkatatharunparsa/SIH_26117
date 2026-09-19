# Confidential synthetic — SIH demo calc for sandbox/H9 (FX-CODE-01)
# Not real plant SoR.

def min_thickness_mm():
    return 8.0

def measured_mm():
    return 7.6

def below_min(measured, minimum):
    return measured < minimum

if __name__ == "__main__":
    m, lo = measured_mm(), min_thickness_mm()
    print({"measured": m, "minimum": lo, "below_min": below_min(m, lo)})
