from algorithms import StayPoint
from entities import GpsFix


def zhen_algorithm(fixes, min_time, dist_tr, verbose=False):
    output = []

    i, j, n = 0, 0, len(fixes)
    done = False

    while i < n:
        if done:
            s = StayPoint.StayPoint(fixes, i, j)
            output.append(s)
            break

        pi = fixes[i]
        j += 1
        while j < n:
            pj = fixes[j]
            distance = GpsFix.distance_diff(pi, pj)
            if distance > dist_tr:
                timespan = GpsFix.time_diff(pi, pj)
                if timespan > min_time:
                    s = StayPoint.StayPoint(fixes, i, j)
                    output.append(s)
                    if verbose:
                        print('New sp created:')
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
