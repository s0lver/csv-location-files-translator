from algorithms import StayPoint
from entities import GpsFix

def montoliou_algorithm(fixes, min_t, max_t, dist_tr, verbose):
    output = []                                 #         ArrayList<StayPoint> output = new ArrayList<>();
    i, j = 0, 0                                 #         int i = 0, j = 0, n = gpsFixes.size();
    n = len(fixes)

    done = False                                #         boolean weAreDone = false;

    while i < n:                                #         while (i<n) {
        if done:                                #             if (weAreDone) {
            s = StayPoint.StayPoint(fixes, i, j)#                 StayPoint sp = StayPoint.createStayPoint(gpsFixes, i, j);
            output.append(s)                    #                 output.add(sp);
            break                               #                 break;
                                                #             }
        pi = fixes[i]
        j = i+1                                 #             j = i + 1;
        while (j < n):                          #             while (j<n){
            pj  = fixes[j]                      #                 pj = gpsFixes.get(j);
                                                #                 // Here is the adaptation that Montoliu does
            pj_minus = fixes[j-1]               #                 pjMinus = gpsFixes.get(j - 1);

            timespan = GpsFix.time_diff(pj_minus, pj)  #                 timespan = timeDifference(pjMinus, pj);
            if (timespan>max_t):                #                 if (timespan > maxTimeTreshold) {
                i = j                           #                     i = j;
                break                           #                     break;
                                                #                 }

            distance = GpsFix.distance_diff(pi, pj)          #                 distance = distance(pi, pj);
            if (distance > dist_tr):            #                 if (distance > distanceTreshold) {
                timespan = GpsFix.time_diff(pi, pj)    #                     timespan = timeDifference(pi, pj);
                                                #                     // If the point is NOT within the interval, then we have moved out of the stay point
                if (timespan > min_t):          #                     if (timespan > minTimeTreshold) {
                    s = StayPoint.StayPoint(fixes, i, j)#                         StayPoint sp = StayPoint.createStayPoint(gpsFixes, i, j);
                    output.append(s)            #                         output.add(sp);
                    if verbose:                 #                         if (verbose) {
                        print('New sp:')        #                             System.out.println("New SP generated. Fixes involved: ");
                        k = i                   #                             for (int k = i; k <= j; k++) {
                        while k<=j:             #                                 System.out.println(gpsFixes.get(k));
                            print(fixes[k])     #                             }
                            k += 1              #                         }
                                                #                     }
                i = j                           #                     i = j;
                break                           #                     break;
                                                #                 }
            j += 1                              #                 j++;
                                                #                 // If this increment finalises the iteration...
            if j == n:                          #                 if (j == n) {
                                                #                     // The we have to stop it
                done = True                     #                     weAreDone = true;
                j -= 1                          #                     j--;
                break                           #                     break;
                                                #                 }
                                                #             }
                                                #         }
    return output                               #         return output;
