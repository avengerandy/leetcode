class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        
        int firstArea = (C - A) * (D - B);
        int secondArea = (G - E) * (H - F);
        int coverAreaW = 0;
        int coverAreaH = 0;
        if (max(A, E) < min(C, G)) {
            coverAreaW = min(C, G) - max(A, E);
        }
        if (max(B, F) < min(D, H)) {
            coverAreaH = min(D, H) - max(B, F);
        }

        return firstArea + secondArea - coverAreaW * coverAreaH;
    }
};