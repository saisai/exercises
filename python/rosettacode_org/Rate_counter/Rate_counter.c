#include <stdio.h>
#include <time.h>

// we only get one-second precision on most systems, as 
// time_t only holds seconds


struct rate_state_s
{
	time_t lastFlush;
	time_t period;
	size_t tickCount;
};

void tic_rate(struct rate_state_s* pRate)
{
	pRate->tickCount += 1;
	time_t now = time(NULL);

	if((now - pRate->lastFlush) >= pRate->period)
	{
		// tps report
		size_t tps = 0.0;
		if(pRate->tickCount > 0)
			tps = pRate->tickCount / (now - pRate->lastFlush);

		printf("%u tics per second.\n", tps);

		// reset
		pRate->tickCount = 0;
		pRate->lastFlush = now;
	}
}


void something_we_do()
{
	volatile size_t anchor = 0;
	size_t x = 0;
	for(x = 0; x < 0xffff; ++x)
	{
		anchor = x;
	}
}

int main()
{
	time_t start = time(NULL);

	struct rate_state_s rateWatch;
	rateWatch.lastFlush = start;
	rateWatch.tickCount = 0;
	rateWatch.period = 5; // Reprot every five seconds.
	
	time_t latest = start;
	// Loop for twenty seconds
	for(latest = start; (latest - start) < 20; latest = time(NULL))
	{
		// Do something
		something_we_do();

		// Note that we did something
		tic_rate(&rateWatch);
	}

	return 0;
}

