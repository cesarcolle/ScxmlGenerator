#include "event.h"

class SM_state {
    SM_state();
    ~SM_state();
    virtual void transition(enum event events);
    virtual void onentry();
    virtual void exitentry();

}