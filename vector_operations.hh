#ifndef __LEARNING_GEM5_HELLO_OBJECT_HH__
#define __LEARNING_GEM5_HELLO_OBJECT_HH__

#include "params/VectorOperations.hh"
#include "sim/sim_object.hh"
#include <iostream>
//#include<vector>
//#include<bits/stdp++.h>
#include <stdio.h>
#include <cmath>

namespace gem5
{

class VectorOperations : public SimObject
{
  private:
    int vectorA[3][1];
    int vectorB[3][1];
    void fun();
    void fun3();
    void fun2();
    void fun1();

    EventFunctionWrapper VectorCrossProduct;
    EventFunctionWrapper NormalizeVector;
    EventFunctionWrapper VectorSubtraction;
    EventFunctionWrapper event;

    int tick1;
    int tick2;
    int tick3;

    int v1i=1;
    int v1j=2;
    int v1k=3;

    int v2i=4;
    int v2j=5;
    int v2k=6;

  public:
    VectorOperations(const VectorOperationsParams &p);
    void startup() override;
};

} // namespace gem5

#endif // __LEARNING_GEM5_HELLO_OBJECT_HH__