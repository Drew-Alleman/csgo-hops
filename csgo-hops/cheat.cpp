
#include "cheat.h"

LPCWSTR DLL_NAME = L"client.dll";
ptrdiff_t dwForceJump = 0x52B8BFC;
ptrdiff_t dwLocalPlayer = 0xDE7964;
ptrdiff_t m_fFlags = 0x104;

class LocalPlayer {

private:
	uintptr_t gameAddress;
	uintptr_t localPlayerAddress;

public:
	bool bhop() {
		int move = moveType();
		if (move == 257 || move == 512 || move == 262 || move == 263 || move == 261) {
			return jump();
		}
		return false;
	}

	bool jump() {
		*reinterpret_cast<int*>(gameAddress + dwForceJump) = 5;
		Sleep(2);
		*reinterpret_cast<int*>(gameAddress + dwForceJump) = 4;
		return true;
	}

	int moveType() {
		return *reinterpret_cast<int*>(localPlayerAddress + m_fFlags);
	}

	void getClientDLLAddress() {
		gameAddress = (DWORD)GetModuleHandle(DLL_NAME);
	}

	void getAddresses() {
		if (gameAddress == NULL)
			getClientDLLAddress();
		if (gameAddress != NULL and localPlayerAddress == NULL)
			updateLocalPlayerAddress();
	}

	void updateLocalPlayerAddress() {
		localPlayerAddress = *reinterpret_cast<uintptr_t*>(gameAddress + dwLocalPlayer);
	}

	bool isValid() {
		return gameAddress != NULL and localPlayerAddress != NULL;
	}
};


void cheat::enableBhop() {
	LocalPlayer localPlayer = LocalPlayer();
	while (true)
	{
		if (!localPlayer.isValid()) {
			localPlayer.getAddresses();
			Sleep(100);
			continue;
		}
		if (GetAsyncKeyState(VK_END))
			break;
		else if (GetAsyncKeyState(VK_SPACE) and localPlayer.bhop()) {
			continue;
		} 
		Sleep(.5);
	}
}