# Gather timline 1 marker data and report to console.

import c4d

doc: c4d.documents.BaseDocument  # The currently active document.
op: c4d.BaseObject | None  # The primary selected object in `doc`. Can be `None`.

def getMarkers(doc):
    # Get the first marker in #doc and loop over them.
    marker: c4d.BaseList2D = c4d.documents.GetFirstMarker(doc)

    while marker:
        # Print out the name, start time(in frames), length(in frames) of the marker and its selection state in Timeline 1.
        mStart = marker[c4d.TLMARKER_TIME].GetFrame(doc.GetFps())
        mLength = marker[c4d.TLMARKER_LENGTH].GetFrame(doc.GetFps())
        rangeTo = mStart + mLength

        print(f"Name: {marker.GetName()}, Start: {mStart}, Length: {mLength}, Range_From: {mStart}, Range_To: {rangeTo}, Selected: {bool(marker.GetNBit(c4d.NBIT_TL1_SELECT))}")
        marker = marker.GetNext()

def main() -> None:
    getMarkers(doc)
    
if __name__ == '__main__':
    main()