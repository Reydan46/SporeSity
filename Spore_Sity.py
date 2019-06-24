def get_work(min_bp):
    max_pr = 0
    max_bp = 0
    out = ''
    A = 1
    for B in range(1, 4):
        for C in range(1, 4):
            for D in range(1, 4):
                for E in range(1, 4):
                    for F in range(1, 4):
                        for G in range(1, 4):
                            for H in range(1, 4):
                                for I in range(1, 4):
                                    for J in range(1, 4):
                                        for K in range(1, 4):
                                            # for L in range(1,4):
                                            pr = 0
                                            bp = 0
                                            # all_sity = [A, B, C, D, E, F, G, H, I, J, K, L]
                                            all_sity = [A, B, C, D, E, F, G, H, I, J, K]
                                            for i in all_sity:
                                                if (i == 2):
                                                    bp += 1
                                                elif (i == 3):
                                                    bp -= 1
                                            # template = [[A, B], [A, E], [A, H], [A, K], [B, C], [B, D], [B, E], [B, K],
                                            #            [C, D], [E, F], [F, G], [G, H], [H, I], [I, J], [K, L]]
                                            template = [[A, B], [A, E], [A, G], [A, K], [A, H], [B, C], [B, D], [C, D],
                                                        [E, F], [G, H], [G, I], [G, J], [H, I]]
                                            for i in template:
                                                i.sort()
                                                if (i[0] == 1) and (i[1] == 2):
                                                    bp += 1
                                                elif (i[0] == 1) and (i[1] == 3):
                                                    pr += 0.3
                                                elif (i[0] == 2) and (i[1] == 3):
                                                    bp -= 1
                                            if (max_pr <= pr) and (bp >= min_bp):
                                                max_pr = pr
                                                max_bp = bp
                                                # out = 'A=' + str(A) + '; B=' + str(B) + '; C=' + str(C) + '; D=' + str(
                                                #    D) + '; E=' + str(E) + '; F=' + str(F) + '; G=' + str(
                                                #    G) + '; H=' + str(H) + '; I=' + str(I) + '; J=' + str(
                                                #    J) + '; K=' + str(K) + '; L=' + str(L)
                                                out = 'A=' + str(A) + '; B=' + str(B) + '; C=' + str(C) + '; D=' + str(
                                                        D) + '; E=' + str(E) + '; F=' + str(F) + '; G=' + str(
                                                        G) + '; H=' + str(H) + '; I=' + str(I) + '; J=' + str(
                                                        J) + '; K=' + str(K)

    print('Pr.=', max_pr, 'Bp.=', max_bp)
    print(out)
    print()


for i in range(1, 6):
    get_work(i)
