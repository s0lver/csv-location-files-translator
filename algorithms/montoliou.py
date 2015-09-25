from entities import GpsFix, StayPoint


def montoliou_algorithm(fixes, min_t, max_t, dist_tr, verbose=False):
    output = []
    i, j, n = 0, 0, len(fixes)
    done = False

    while i < n:
        if done:
            s = StayPoint.StayPoint(fixes, i, j)
            output.append(s)
            break
        pi = fixes[i]
        j = i + 1
        while j < n:
            pj = fixes[j]
            pj_minus = fixes[j - 1]

            timespan = GpsFix.time_diff(pj_minus, pj)
            if timespan > max_t:
                i = j
                break

            distance = GpsFix.distance_diff(pi, pj)
            if distance > dist_tr:
                timespan = GpsFix.time_diff(pi, pj)
                if timespan > min_t:
                    s = StayPoint.StayPoint(fixes, i, j)
                    output.append(s)
                    if verbose:
                        print('New staypoint created')
                        k = i
                        while k <= j:
                            print(fixes[k])
                            k += 1
                i = j
                break

            j += 1
            if j == n:
                done = True
                j -= 1
                break

    return output
