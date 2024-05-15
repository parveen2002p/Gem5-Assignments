#include "learning_gem5/part2/vector_operations.hh"
#include "base/trace.hh"
#include "debug/RESULTCROSS.hh"
#include "debug/NORMALIZE.hh"
#include "debug/RESULTSUB.hh"
#include "debug/VECTOR.hh"
#include <iostream>
#include <cmath>
//#include<vector>
//#include<bits/stdp++.h>

namespace gem5
{

VectorOperations::VectorOperations(const VectorOperationsParams &params) :
    SimObject(params), event([this]{fun();}, name())
    ,VectorCrossProduct([this]{fun1();}, name())
    ,NormalizeVector([this]{fun2();}, name())
    ,VectorSubtraction([this]{fun3();}, name()),
    tick1(params.tick1),
    tick2(params.tick2),
    tick3(params.tick3),
    v1i(params.v1i),
    v1j(params.v1j),
    v1k(params.v1k),
    v2i(params.v2i),
    v2j(params.v2j),
    v2k(params.v2k)
{
    //std::cout << "Hello! From Custom SimObject!" << std::endl;
    vectorA[0][0]=v1i;
    vectorA[1][0]=v1j;
    vectorA[2][0]=v1k;

    vectorB[0][0]=v2i;
    vectorB[1][0]=v2j;
    vectorB[2][0]=v2k;
}

void VectorOperations::fun()
{
    DPRINTF(VECTOR, "Displaying Vectors\n");
    DPRINTF(VECTOR, "Vector 1 : (%d, %d, %d)\n", vectorA[0][0], vectorA[1][0], vectorA[2][0]);
    DPRINTF(VECTOR, "Vector 2 : (%d, %d, %d)\n", vectorB[0][0], vectorB[1][0], vectorB[2][0]);
}

void VectorOperations::startup()
{
    schedule(event, 50);
    schedule(VectorCrossProduct, tick1);
    schedule(NormalizeVector, tick2);
    schedule(VectorSubtraction, tick3);
}

void VectorOperations::fun1() {
        DPRINTF(RESULTCROSS, "Displaying VectorCrossProduct\n");
        int tp[3];
        
        tp[0] = vectorA[1][0] * vectorB[2][0] - vectorA[2][0] * vectorB[1][0];
        tp[1] = - (vectorA[0][0] * vectorB[2][0] - vectorA[2][0] * vectorB[0][0]);
        tp[2] = vectorA[0][0] * vectorB[1][0] - vectorA[1][0] * vectorB[0][0];
       
        DPRINTF(RESULTCROSS, "Resultant Vector: (%d, %d, %d)\n",tp[0], tp[1], tp[2]);
    }

void VectorOperations::fun2() {
        DPRINTF(NORMALIZE, "Displaying Normalized Vectors\n");

        float tp[3];
        double magA = sqrt(vectorA[0][0] * vectorA[0][0] + vectorA[1][0] * vectorA[1][0] + vectorA[2][0] * vectorA[2][0]);
        tp[0] = vectorA[0][0] / magA;
        tp[1] = vectorA[1][0] / magA;
        tp[2] = vectorA[2][0] / magA;
        DPRINTF(NORMALIZE, "Normalized Vector A: (%f, %f, %f)\n",tp[0], tp[1], tp[2]);

        double magB = sqrt(vectorB[0][0] * vectorB[0][0] + vectorB[1][0] * vectorB[1][0] + vectorB[2][0] * vectorB[2][0]);
        tp[0] = vectorB[0][0] / magB;
        tp[1] = vectorB[1][0] / magB;
        tp[2] = vectorB[2][0] / magB;
        DPRINTF(NORMALIZE, "Normalized Vector B: (%f, %f, %f)\n",tp[0], tp[1], tp[2]);
    }

void VectorOperations::fun3() {
        DPRINTF(RESULTSUB, "Displaying VectorSubtraction\n");
        int tp[3];
        for (int i = 0; i < 3; ++i) {
            tp[i] = vectorA[i][0] - vectorB[i][0];
        }
        DPRINTF(RESULTSUB, "Resultant Vector: (%d, %d, %d)\n",tp[0], tp[1], tp[2]);
    }

} // namespace gem5